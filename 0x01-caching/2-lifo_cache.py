#!/usr/bin/env python3

"""Basecaching module"""

from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Caching system class"""

    def __init__(self):
        """Initializes the cache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assigns key value to cache_data"""
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                log, _ = self.cache_data.popitem(True)
                print("DISCARD:", log)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Returns value of key"""
        if key is None:
            return None
        return self.cache_data.get(key, None)
