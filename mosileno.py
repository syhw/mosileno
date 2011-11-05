import os
import logging
from urllib import quote, unquote
import httplib2
import simplejson as json

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
    h = httplib2.Http(".cache")
    items = []
    headers={'cache-control': 'max-age=180'}
    link="http://api.ihackernews.com/page"
    if (request.GET.get('nextId') is not None):
        link += '/' + request.GET.get('nextId')
    resp, content = h.request(link, headers=headers)
    items.extend(json.loads(content)['items'])
    return {'items': items,
            'username': 'toto'}

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

