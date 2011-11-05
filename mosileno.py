import os
import logging
from urllib import quote, unquote

from pyramid.config import Configurator
from pyramid.session import UnencryptedCookieSessionFactoryConfig
from pyramid.view import view_config
from pyramid.response import Response

from mongokit import Connection
from timer import Timer

from paste.httpserver import serve

logging.basicConfig()
log = logging.getLogger(__file__)

here = os.path.dirname(os.path.abspath(__file__))

@view_config(route_name='root', renderer='hn.mako')
def root(request):
    #items = []
    items = [{'url': "http://www.yahoo.fr",
        #'url': request.route_url('frame', 
        #    url=quote("http://www.yahoo.fr", safe="")),
        'domain': "yahoo.com",
        'title': "Yahoo",
        'points': 666,
        'author': "Oohay",
        'age': "18 years",
        'num_comments': 69}]
    return {'items': items}

@view_config(route_name='frame', renderer='frame.mako')
def frame(request):
    return {'url': unquote(request.GET.get('url'))}

@view_config(route_name='timer_start')
def timer_start(request):
    t = request.registry.settings['db'].hdparis114.timers.Timer(request.matchdict['user'],
            request.GET.get('url'))
    t.save()
    return Response(t._id)

@view_config(route_name='timer_restart')
def timer_restart(request):
    t = request.registry.settings['db'].Timer.find({'_id': 
            request.matchdict['id']})
    t.start(request.matchdict['time'])
    t.save()
    return Response("OK")

@view_config(route_name='timer_stop')
def timer_stop(request):
    t = request.registry.settings['db'].Timer.find({'_id': 
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
    settings['db'] = con
    # session factory
    session_factory = UnencryptedCookieSessionFactoryConfig('secret')
    # configuration setup
    config = Configurator(settings=settings, session_factory=session_factory)
    config.add_static_view('static', 'static/')
    config.add_route('root', '/')
    config.add_route('frame', '/frame')
    config.add_route('timer_start', '/timer_start/{user}')
    config.add_route('timer_restart', '/timer_restart/{id}')
    config.add_route('timer_stop', '/timer_stop/{id}')
    config.scan()
    # serve app
    app = config.make_wsgi_app()
    serve(app, host='0.0.0.0')

