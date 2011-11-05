import os
import logging
from urllib import quote, unquote
import httplib2
import simplejson as json
from urlparse import urlparse


from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.decorator import reify
from pyramid.request import Request
from pyramid.response import Response
from pyramid.security import unauthenticated_userid
from pyramid.session import UnencryptedCookieSessionFactoryConfig
from pyramid.view import view_config

from mongokit import Connection

from security import User, populate, get_user, groupfinder
from timer import Timer

from paste.httpserver import serve

logging.basicConfig()
log = logging.getLogger(__file__)

here = os.path.dirname(os.path.abspath(__file__))
#domainre = re.compile(r"http://[^.]*\.([^.]*\.[^/]*)/.*")

class RequestWithUserAttribute(Request):

     @reify
     def user(self):
         dbconn = self.registry.settings['db']
         userid = unauthenticated_userid(self)
         if userid is not None:
             return get_user(self, userid)

@view_config(route_name='root', renderer='hn.mako')
def root(request):
    h = httplib2.Http(".cache")
    items = []
    headers={'cache-control': 'max-age=180'}
    link="http://api.ihackernews.com/page"
    if (request.GET.get('nextId') is not None):
        link += '/' + request.GET.get('nextId')
    resp, content = h.request(link, headers=headers)
    items.extend(json.loads(content)['items'])
    for item in items:
        tmp = str(urlparse(item['url']).hostname)
        item['domain'] = tmp[4:] if tmp.startswith('www.') else tmp
    return {'items': items,
            'username': unauthenticated_userid(request)}

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
    con.register([Timer, User])
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

    config.set_request_factory(RequestWithUserAttribute)

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

    # Init user data
    populate(settings['db'])

    # serve app
    app = config.make_wsgi_app()
    serve(app, host='0.0.0.0')
