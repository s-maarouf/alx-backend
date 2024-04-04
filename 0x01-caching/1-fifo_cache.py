#!/usr/bin/env python3

"""Basecaching module"""

from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Caching system class"""

    def __init__(self):
        """Initializes the cache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assigns key value to cache_data"""
        if key is None or item is None:
            pass
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            log, _ = self.cache_data.popitem(False)
            print("DISCARD:", log)

    def get(self, key):
        """Returns value of key"""
        if key is None or key is isinstance:
            return None
        else:
          return self.cache_data[key]
