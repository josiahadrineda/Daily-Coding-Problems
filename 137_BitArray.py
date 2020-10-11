# All operations (except repr) are O(1)
class BitArray:
    def __init__(self, size):
        self.size = size
        self.ba = {}

    def __repr__(self):
        l = []
        for i in range(self.size):
            l.append(self.ba.get(i, 0))
        return str(l)

    def set(self, i, val):
        if 0 <= i < self.size:
            self.ba[i] = val

    def get(self, i):
        if 0 <= i < self.size:
            return self.ba.get(i, 0)

ba = BitArray(10)
assert ba.get(9) == 0
assert ba.set(9, 1) == None
assert ba.get(9) == 1
assert ba.get(10) == None
assert repr(ba) == '[0, 0, 0, 0, 0, 0, 0, 0, 0, 1]'