from itertools import combinations
from functools import lru_cache

def denominations(ways):
    """Given a list of integers WAYS, where WAYS[i] represents the number of ways one
    can produce i units of change, determines the denominations that that must be in use.

    >>> denominations([1, 0, 1, 1, 1])
    [2, 3]
    >>> denominations([1, 0, 1, 1, 2])
    [2, 3, 4]
    >>> denominations([1, 0, 1, 1, 3])
    []
    """
    assert ways, 'WAYS cannot be an empty list.'

    def denom_recur(denoms):
        @lru_cache(maxsize=None)
        def num_ways(denoms, change):
            if not denoms or change < 0:
                return 0
            elif change == 0:
                return 1
            return num_ways(denoms[1:], change) + num_ways(denoms, change - denoms[0])
        return [num_ways(denoms, c) for c in range(n)]

    n = len(ways)

    denoms = [d for d in range(1, n) if ways[d]]
    for l in range(len(denoms), 0, -1):
        for denoms_combo in list(combinations(denoms, l)):
            if denom_recur(denoms_combo) == ways:
                return list(denoms_combo)
    return []