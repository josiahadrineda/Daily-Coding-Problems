"""
IMPORTANT REALIZATION:
    - Two references to next are allowed so long as they aren't the same type
    (function and function/generator and generator).
"""

class TwoDimensionalIterator:
    """An iterator for 2-dimensional arrays.

    >>> i = TwoDimensionalIterator([[1, 2], [3], [], [4, 5, 6]])
    >>> i.next()
    1
    >>> i.has_next()
    True
    >>> i.next()
    2
    >>> i.has_next()
    True
    >>> i.next()
    3
    >>> i.has_next()
    True
    >>> i.next()
    4
    >>> i.has_next()
    True
    >>> i.next()
    5
    >>> i.has_next()
    True
    >>> i.next()
    6
    >>> i.has_next()
    False
    >>> i.next()
    """

    def __init__(self, arr):
        self.arr = arr
        self.gen = self.generator()
        self.next_el = next(self.gen)

    def generator(self):
        for subarr in self.arr:
            for el in subarr:
                yield el

    def next(self):
        el = self.next_el
        try:
            self.next_el = next(self.gen)
        except StopIteration:
            self.next_el = None
        return el

    def has_next(self):
        return self.next_el is not None