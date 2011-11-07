from mongokit import Document


class User(Document):

    __collection__ = 'users'
    __database__ = 'hackernoise'

    structure = {
        'username': unicode,
        'password': unicode,
    }

    use_dot_notation = True


USERS = {
    u'ronnix': u'aighuS6Hiec6eiGh',
    u'snippyhollow': u'Aichoth4bid0iel0',
}


def populate(dbconn):
    for username, password in USERS.items():
        user = dbconn.users.User.find_one({'username': username})
        if not user:
            user = dbconn.users.User()
            user.username = username
            user.password = password
            user.save()


def get_user(request, username):
    dbconn = request.registry.settings['db']
    return dbconn.users.User.find_one({'username': username})


def groupfinder(request, username):
    if request.user is not None:
        return [u'users']
    return None
