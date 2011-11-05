from time import time
from mongokit import Document

class Timer(Document):
    #__collection__ = 'timers'
    #__database__ = 'hdparis114'
    structure = {
            'url': unicode,
            'user': int,
            'elapsed': int,
            'start_time': int
            }

    def __init__(self, url, user, start_time=None):
        Document.__init__(self)
        self.elapsed = 0
        self.url = url
        self.user = user
        self.start(start_time)

    def start(self, start_time=None):
        if start_time is None:
            self.start_time = time()
        else:
            self.start_time = start_time

    def stop(self):
        if (self.start_time is not None):
            self.elapsed += time() - self.start_time
        self.start_time = None

