from time import time

class Timer(object):
    def __init__(self, start_time=None):
        self.elapsed = 0
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

