#!/usr/bin/env python3
"""defines a class called `BasicCace`"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A caching system"""

    def __init__(self):
        """Initializes the class attributes."""
        super().__init__()

    def put(self, key, item):
        """Adds an item in the cache."""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Gets an item by key."""
        return self.cache_data.get(key, None)
