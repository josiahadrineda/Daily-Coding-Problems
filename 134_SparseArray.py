class SparseArray:
    def __init__(self, arr, size):
        self.dict = {}
        for i, el in enumerate(arr):
            self.dict[i] = el
        self.size = size

    def __repr__(self):
        return str(self.dict)

    def set(self, i, val):
        if i < self.size:
            self.dict[i] = val

    def get(self, i):
        if i < self.size:
            return self.dict[i]

sa = SparseArray([0] * 200, 200)
for i in range(0, 200, 2):
    sa.set(i, 1)
assert sa.get(198) == 1
assert sa.get(199) == 0
assert not sa.get(200)