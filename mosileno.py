import os
import logging
from urllib import quote, unquote

from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.security import unauthenticated_userid
from pyramid.session import UnencryptedCookieSessionFactoryConfig
from pyramid.response import Response
from pyramid.view import view_config

from mongokit import Connection

from security import groupfinder
from timer import Timer

from paste.httpserver import serve

logging.basicConfig()
log = logging.getLogger(__file__)

here = os.path.dirname(os.path.abspath(__file__))

@view_config(route_name='root', renderer='hn.mako')
def root(request):
    items = [
        {
            'url': "http://www.yahoo.fr",
            'domain': "yahoo.fr",
            'title': "Yahoo",
            'points': 666,
            'author': "Oohay",
            'age': "18 years",
            'num_comments': 69
        },
        {
            'url': "http://www.techcrunch.com",
            'domain': "techcrunch.com",
            'title': "Techcrunch",
            'points': 456,
            'author': "bob",
            'age': "5 months",
            'num_comments': 42
        }
    ]
    return {
        'items': items,
        'username': unauthenticated_userid(request)
    }

@view_config(route_name='frame', renderer='frame.mako')
def frame(request):
    return {'url': unquote(request.GET.get('url'))}

@view_config(route_name='timer_start')
def timer_start(request):
    t = request.registry.settings['db'].timers.Timer()
    t.init(request.matchdict['user'], request.GET.get('url'))
    t.save()
    return Response(str(t._id))

@view_config(route_name='timer_restart')
def timer_restart(request):
    t = request.registry.settings['db'].timers.Timer.find({'_id':
            request.matchdict['id']})
    t.start(request.matchdict['time'])
    t.save()
    return Response("OK")

@view_config(route_name='timer_stop')
def timer_stop(request):
    t = request.registry.settings['db'].timers.Timer.find({'_id':
            request.matchdict['id']})
    t.stop()
    t.save()
    return Response("OK")

if __name__ == '__main__':
    # configuration settings
    settings = {}
    settings['reload_all'] = True
    settings['debug_all'] = True
    settings['debug_templates'] = True
    settings['debug_routematch'] = True
    settings['includes'] = ["pyramid_debugtoolbar"]
    settings['mako.directories'] = os.path.join(here, 'templates')
    con = Connection('mongodb://hdparis114:f41922d68004e@hackday.mongohq.com:27017/hdparis114')
    con.register([Timer])
    settings['db'] = con.hdparis114

    # session factory
    session_factory = UnencryptedCookieSessionFactoryConfig('secret')

    # authentication and authorization
    cookie_secret = 'xohqu2aiPi4qui0aeM6uengieghee9ul'
    authentication_policy = AuthTktAuthenticationPolicy(cookie_secret,
        cookie_name='mosileno_auth', callback=groupfinder)
    authorization_policy = ACLAuthorizationPolicy()

    # configuration setup
    config = Configurator(settings=settings,
                          session_factory=session_factory,
                          authentication_policy=authentication_policy,
                          authorization_policy=authorization_policy)

    # routes and views
    config.add_static_view('static', 'static/')
    config.add_route('root', '/')
    config.add_route('frame', '/frame')
    config.add_route('timer_start', '/timer_start/{user}')
    config.add_route('timer_restart', '/timer_restart/{id}')
    config.add_route('timer_stop', '/timer_stop/{id}')
    config.add_route('login', '/login')
    config.add_view('auth.login',
                    context='pyramid.httpexceptions.HTTPForbidden',
                    renderer='login.mako')
    config.add_view('auth.login',
                    route_name='login',
                    renderer='login.mako')
    config.add_route('logout', '/logout')
    config.add_view('auth.logout', route_name='logout')
    config.scan()

    # serve app
    app = config.make_wsgi_app()
    serve(app, host='0.0.0.0')
