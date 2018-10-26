import datetime
import random

class Cache:

    def __init__(self):
        # Constructor
        self.cache = {}
        self.MaxSize = 5

    def update(self, key, value):
        # Update cache and remove oldest item, when size reaches maximum
        if key not in self.cache and len(self.cache) >= self.MaxSize:
            self.removeOldCache()

        self.cache[key] = {'Added time': datetime.datetime.now().isoformat(),
                           'value': value}

    def removeOldCache(self):
        # Remove oldest item from cache
        oldest_entry = None
        for key in self.cache:
            if oldest_entry is None:
                oldest_entry = key
            elif self.cache[key]['Added time'] < self.cache[oldest_entry]['Added time']:
                oldest_entry = key
        self.cache.pop(oldest_entry)

    def __contains__(self, key):
        # Returns Boolean value, whether key is in the cache
        return key in self.cache

    def isEmpty(self):
        # checking, whether cache is Empty
        return self.cache == 0

    def size(self):
        # Returns total size of cache
        return len(self.cache)

    def viewCache(self):
        return self.cache