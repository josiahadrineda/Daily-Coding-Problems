from math import floor

def is_power_of_four(n):
    """Given a positive 32-bit integer N, determines whether N is a power of four
    in faster than O(log N) time.

    >>> is_power_of_four(16)
    True
    >>> is_power_of_four(64)
    False
    >>> is_power_of_four(62742241)
    True
    """
    assert 0 < n < (1<<31) - 1, 'N must be a positive 32-bit integer.'

    return floor(n**(1/4)) == n**(1/4)

def is_power_binary_search(n):
    """Given a positive 32-bit integer N, determines whether N is a power of four
    in O(log N) time.

    >>> is_power_of_four(16)
    True
    >>> is_power_of_four(64)
    False
    >>> is_power_of_four(62742241)
    True
    """
    assert 0 < n < (1<<31) - 1, 'N must be a positive 32-bit integer.'

    def fourth_power(n):
        return n * n * n * n

    if n == 1:
        return True

    l, r = 0, n // 4
    while l <= r:
        m = r + (l - r) // 2
        fp = fourth_power(m)
        if fp == n:
            return True
        elif fp > n:
            r = m - 1
        else:
            l = m + 1
    return False