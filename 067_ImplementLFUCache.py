from collections import defaultdict

class LFUCache:
    def __init__(self, capacity):
        self.cache = defaultdict(list)
        self.freqs = defaultdict(list)
        self.capacity = capacity
        self.min_freq = 0
        self.count = 0

    def set(self, key, value):
        if self.capacity == 0:
            return
        
        if key in self.cache:
            val,freq = self.cache[key]
            self.cache[key] = (value, freq+1)

            self.freqs[freq].remove(key)
            self.freqs[freq+1].insert(0, key)

            if len(self.freqs[freq]) == 0 and freq == self.min_freq:
                self.min_freq += 1

            return

        if self.count == self.capacity:
            key_to_remove = self.freqs[self.min_freq].pop()
            del self.cache[key_to_remove]
            self.count -= 1

        self.cache[key] = (value, 1)
        self.freqs[1].insert(0, key)
        self.count += 1
        self.min_freq = 1
        return

    def get(self, key):
        if key not in self.cache:
            return -1
        
        val,freq = self.cache[key]
        self.cache[key] = (val, freq+1)
        
        self.freqs[freq].remove(key)
        self.freqs[freq+1].insert(0, key)

        if len(self.freqs[freq]) == 0 and freq == self.min_freq:
            self.min_freq += 1

        return val

cache = LFUCache(2)

assert cache.set(1, 1) == None
assert cache.set(2, 2) == None
assert cache.get(1) == 1
assert cache.set(3, 3) == None
assert cache.get(2) == -1
assert cache.get(3) == 3
assert cache.set(4, 4) == None
assert cache.get(1) == -1
assert cache.get(3) == 3
assert cache.get(4) == 4

cache = LFUCache(2)

assert cache.set(3,1) == None
assert cache.set(2,1) == None
assert cache.set(2,2) == None
assert cache.set(4,4) == None
assert cache.get(2) == 2

cache = LFUCache(2)

assert cache.set(2,1) == None
assert cache.set(2,2) == None
assert cache.get(2) == 2
assert cache.set(1,1) == None
assert cache.set(2,1) == None
assert cache.get(2) == 1

cache = LFUCache(3)

assert cache.set(1,1) == None
assert cache.set(2,2) == None
assert cache.set(3,3) == None
assert cache.set(4,4) == None
assert cache.get(4) == 4
assert cache.get(3) == 3
assert cache.get(2) == 2
assert cache.get(1) == -1
assert cache.set(5,5) == None
assert cache.get(1) == -1
assert cache.get(2) == 2
assert cache.get(3) == 3
assert cache.get(4) == -1
assert cache.get(5) == 5