# https://www.youtube.com/watch?v=6aHmj9ihjMY&ab_channel=Errichto

def bitwise_and(m, n):
    """Computes the bitwise AND (&) of all integers between nonnegative integers
    M and N, inclusive.

    >>> bitwise_and(5, 7)
    4
    """
    assert m >= 0, 'M must be a nonnegative integer.'
    assert n >= 0, 'N must be a nonnegative integer.'
    assert m <= n, 'M must be less than or equal to N.'

    res = 0
    for bit in range(30, -1, -1):
        if (m & (1 << bit)) != (n & (1 << bit)):
            break
        else:
            res |= (m & (1 << bit))
    return res