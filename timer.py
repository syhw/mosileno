from time import time
from mongokit import Document

class Timer(Document):

    __collection__ = 'timers'
    __database__ = 'hdparis114'

    structure = {
        'url': unicode,
        'user': unicode,
        'elapsed': int,
        'start_time': int
    }

    default_values = {
        'elapsed': 0,
    }

    use_dot_notation = True

    def init(self, user, url, start_time=None):
        self.user = unicode(user)
        self.url = unicode(url)
        self.start(start_time)

    def start(self, start_time=None):
        if start_time is None:
            self.start_time = int(time())
        else:
            self.start_time = int(start_time)

    def stop(self):
        if (self.start_time is not None):
            self.elapsed += int(time()) - self.start_time
        self.start_time = None
