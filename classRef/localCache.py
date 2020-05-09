import shelve
from contextlib import closing


class local_cache:
    def __init__(self, cache='default'):
        self.cache = cache

    def __setitem__(self, key, value):
        """
        key: 变量名
        value: 变量值
        cache: 缓存名
        """
        with closing(shelve.open(self.cache, 'c')) as shelf:
            shelf[key] = value

    def __getitem__(self, key):
        """
        key : 变量名
        return：变量值
        """
        with closing(shelve.open(self.cache, 'r')) as shelf:
            return shelf[key]
