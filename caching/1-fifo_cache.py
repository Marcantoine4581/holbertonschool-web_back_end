#!/usr/bin/python3
""" 1. FIFO caching """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """class FIFOCache that inherits from BaseCaching
    and is a caching system
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache and discard the first item put in cache
        if the number of items in self.cache_data is higher
        that BaseCaching.MAX_ITEMS
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                key_discarded = list(self.cache_data)[0]
                self.cache_data.pop(key_discarded)
                print("DISCARD: " + key_discarded)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
