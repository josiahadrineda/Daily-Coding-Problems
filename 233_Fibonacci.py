def fib(n):
    """Given a positive integer N, returns the Nth fibonacci number in O(1) space.

    >>> [fib(i) for i in range(1, 11)]
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    """
    assert n > 0, 'N must be a positive integer.'

    a, b = 0, 1
    while n:
        a, b, n = b, a + b, n - 1
    return a