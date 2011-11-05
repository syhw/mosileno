import os
import logging
from urllib import quote, unquote

from pyramid.config import Configurator
from pyramid.session import UnencryptedCookieSessionFactoryConfig

from pyramid.view import view_config

from paste.httpserver import serve

logging.basicConfig()
log = logging.getLogger(__file__)

here = os.path.dirname(os.path.abspath(__file__))

@view_config(route_name='frame', renderer='frame.mako')
def frame(request):
    return {'url': unquote(request.matchdict['url'])}

@view_config(route_name='root', renderer='hn.mako')
def root(request):
    #items = []
    items = [{#{'url': "http://www.yahoo.fr",
        'url': request.route_url('frame', 
            url=quote("http://www.yahoo.fr", safe="")),
        'domain': "yahoo.com",
        'title': "Yahoo",
        'points': 666,
        'author': "Oohay",
        'age': "18 years",
        'num_comments': 69}]
    return {'items': items}

if __name__ == '__main__':
    # configuration settings
    settings = {}
    settings['reload_all'] = True
    settings['debug_all'] = True
    settings['mako.directories'] = os.path.join(here, 'templates')
    # session factory
    session_factory = UnencryptedCookieSessionFactoryConfig('secret')
    # configuration setup
    config = Configurator(settings=settings, session_factory=session_factory)
    config.add_route('root', '/')
    config.add_route('frame', '/frame/{url}')
#    config.add_route('timer_start', '/timerstart/{time}')
#    config.add_route('timer_restart', '/timerrestart/{id}/{time}')
#    config.add_route('timer_stop', '/timerstop/{id}')
    config.scan()
    # serve app
    app = config.make_wsgi_app()
    serve(app, host='0.0.0.0')
