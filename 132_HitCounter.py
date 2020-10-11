class HitCounter:
    """A hit counter for some arbitrary object.
    """

    def __init__(self):
        self.hit_counter = {} # {timestamp : num_hits}
        self.tot = 0

    def record(self, timestamp):
        """Records a hit that happened at timestamp.
        """
        if self.hit_counter.get(timestamp):
            self.hit_counter[timestamp] += 1
        else:
            self.hit_counter[timestamp] = 1
        self.tot += 1

    def total(self):
        """Returns the total number of hits recorded.
        """
        return self.tot

    def range(self, lower, upper):
        """Returns the number of hits that occurred
        between timestamps lower and upper (inclusive).
        """
        tot = 0
        for i in range(lower, upper + 1):
            if self.hit_counter.get(i):
                tot += self.hit_counter[i]
        return tot

hc = HitCounter()
for _ in range(5): hc.record(1)
for _ in range(4): hc.record(2)
for _ in range(3): hc.record(3)
for _ in range(2): hc.record(4)
for _ in range(1): hc.record(5)
assert hc.total() == 15
assert hc.range(0, 6) == 15
assert hc.range(1, 3) == 12