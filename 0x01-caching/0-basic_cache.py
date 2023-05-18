#!/usr/bin/python3
""" return the value in self.cache_data linked to key """


class BasicCache(BaseCaching):
    """ cached function """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
