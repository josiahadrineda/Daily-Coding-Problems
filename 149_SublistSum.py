class List:
    """A modified List class with an additional sublist sum method.

    >>> l = List([1, 2, 3, 4, 5])
    >>> l.sum(1, 3) # sum([2, 3])
    5
    """

    def __init__(self, l):
        self.l = l
        
        total = 0
        self.sums = {0:total}
        for ind, el in enumerate(self.l, start=1):
            total += el
            self.sums[ind] = total

    def sum(self, i, j):
        if i < 0 or i > len(self.l) or j < 0 or j > len(self.l) or i >= j:
            return 0
        return self.sums[j] - self.sums[i]