#!/usr/bin/python3
""" inherits from BaseCaching and is a caching system """


class LIFOCache(BaseCaching):
    """ Cache inheriter """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = next(reversed(self.cache_data))

            del self.cache_data[last_key]
            print("DISCARD:", last_key)

        self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
