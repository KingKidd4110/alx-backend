#!/usr/bin/python3
""" inherits from BaseCaching and is a caching system """


class MRUCache(BaseCaching):
    """ Inheriter """
    def __init__(self):
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.usage_order[-1]

            del self.cache_data[mru_key]
            self.usage_order.remove(mru_key)
            print("DISCARD:", mru_key)

        self.cache_data[key] = item
        self.usage_order.append(key)

    def get(self, key):
        """ Get an item from the cache """
        if key is None or key not in self.cache_data:
            return None

        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
