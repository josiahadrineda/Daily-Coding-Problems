from math import sqrt
from functools import lru_cache

def min_operations(n):
    """Given a positive integer N, returns the minimum number of operations required to
    reach 1, where the operations are defined as follows:
    
    1. N can be decremented to N - 1
    2. If A * B = N, N may become max(A, B) < N

    >>> min_operations(100)
    5
    >>> min_operations(64)
    4
    """
    assert n > 0, 'N must be a positive integer.'

    def factors(n):
        f = []
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                f.append((i, n // i))
        return f

    @lru_cache(maxsize=None)
    def dfs(n):
        if n == 1:
            return 0
        else:
            res = float('inf')
            f = factors(n)
            if f:
                res = min([dfs(b) for a,b in f])
            return 1 + min(res, dfs(n - 1))
    return dfs(n)