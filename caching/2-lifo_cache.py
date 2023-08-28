#!/usr/bin/python3
""" 2. LIFO Caching """
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """class LIFOCache that inherits from BaseCaching
    and is a caching system
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache and discard the last item put in cache
        if the number of items in self.cache_data is higher
        that BaseCaching.MAX_ITEMS
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_key = list(self.cache_data)[-2]
                self.cache_data.pop(last_key)
                print("DISCARD: " + last_key)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
