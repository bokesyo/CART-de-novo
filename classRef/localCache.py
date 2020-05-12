import shelve
from contextlib import closing


class local_cache:
    def __init__(self, cache='default'):
        self.cache = cache

    def __setitem__(self, key, value):
        with closing(shelve.open(self.cache, 'c')) as shelf:
            shelf[key] = value

    def __getitem__(self, key):
        with closing(shelve.open(self.cache, 'r')) as shelf:
            return shelf[key]
