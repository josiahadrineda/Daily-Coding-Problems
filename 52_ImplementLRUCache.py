from collections import OrderedDict

class LRU_Cache:
    def __init__(self, n):
        self.n = n
        self.cache = OrderedDict()
    
    def print_cache(self):
        print(self.cache)

    def set(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key, last=False)
        if len(self.cache) > self.n:
            self.cache.popitem()

    def get(self, key):
        try:
            value = self.cache[key]
        except KeyError:
            return -1
        self.cache.move_to_end(key, last=False)
        return value

#Driver code
lru = LRU_Cache(2)

assert lru.set(1,1) == None
assert lru.set(2,2) == None
assert lru.get(1) == 1
assert lru.set(3,3) == None
assert lru.get(2) == -1
assert lru.set(4,4) == None
assert lru.get(1) == -1
assert lru.get(3) == 3
assert lru.get(4) == 4