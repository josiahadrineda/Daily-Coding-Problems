def add_xor_pairs(m, n):
    """Given two positive integers M and N, returns the total number of positive integer
    pairs (A, B) that satisfy the following conditions:
    
    1. A + B = M
    2. A XOR B = N

    >>> add_xor_pairs(100, 4)
    1
    """
    assert m > 0, 'M must be a positive integer.'
    assert n > 0, 'N must be a positive integer.'

    res = 0
    if n >= m:
        return res
    for a in range(1, m // 2):
        b = m - a
        if a ^ b == n:
            res += 1
    return res