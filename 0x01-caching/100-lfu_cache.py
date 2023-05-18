#!/usr/bin/python3
""" LFUCache that inherits from BaseCaching and is a caching system """


class LFUCache(BaseCaching):
    """Inheriter """
    def __init__(self):
        super().__init__()
        self.usage_count = {}
        self.usage_order = []

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            min_count = min(self.usage_count.values())
            least_frequent_keys = [
                key for key, count in self.usage_count.items() if count == min_count
            ]

            lru_key = None
            if len(least_frequent_keys) > 1:
                for used_key in self.usage_order:
                    if used_key in least_frequent_keys:
                        lru_key = used_key
                        break

            del self.cache_data[lru_key]
            del self.usage_count[lru_key]
            self.usage_order.remove(lru_key)
            print("DISCARD:", lru_key)

        self.cache_data[key] = item
        self.usage_count.setdefault(key, 0)
        self.usage_count[key] += 1
        self.usage_order.append(key)

    def get(self, key):
        """ Get an item from the cache """
        if key is None or key not in self.cache_data:
            return None

        self.usage_count[key] += 1
        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
