from pyramid.httpexceptions import HTTPFound
from pyramid.security import remember
from pyramid.security import forget

from security import get_user


def login(request):
    """
    Login form and handler
    """
    login_url = request.route_url('login')
    referrer = request.url
    if referrer == login_url:
        referrer = '/' # never use the login form itself as came_from
    came_from = request.params.get('came_from', referrer)
    message = ''
    login = ''
    password = ''
    if 'form.submitted' in request.params:
        login = request.params['login']
        password = request.params['password']
        user = get_user(request, login)
        if user and (user.password == password):
            headers = remember(request, login)
            return HTTPFound(location = came_from,
                             headers = headers)
        message = 'Failed login'

    return dict(
        message = message,
        url = request.application_url + '/login',
        came_from = came_from,
        login = login,
        password = password,
        )


def logout(request):
    """
    Logout handler
    """
    headers = forget(request)
    return HTTPFound(location = request.route_url('root'),
                     headers = headers)
