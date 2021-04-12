from functools import lru_cache

def square_sum(n):
    """Given a positive integer N, returns the minimum number of squares needed to sum
    to N.

    >>> for i in range(1, 11):
    ...     print(square_sum(i))
    1
    2
    3
    1
    2
    3
    4
    2
    1
    2
    """
    assert n > 0, 'N must be a positive integer.'

    @lru_cache(maxsize=None)
    def dfs(n):
        if n < 0:
            return float('inf')
        elif n == 0:
            return 0
        return 1 + min(dfs(n - square) for square in squares)

    squares = []
    i = 1
    while i*i < n:
        squares.insert(0, i*i)
        i += 1

    if i*i == n:
        return 1
    squares.insert(0, i*i)
    return dfs(n)