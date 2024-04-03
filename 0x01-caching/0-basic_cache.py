#!/usr/bin/env python3

"""Basecaching module"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Caching system class"""

    def put(self, key, item):
        """Assigns item to cache_data"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Returns key valur to cache_data"""
        return self.cache_data.get(key, None)
