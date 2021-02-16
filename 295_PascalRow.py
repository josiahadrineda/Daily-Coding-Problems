def pascal_row(k):
    """Given a positive integer K, computes the Kth row of Pascal's Triangle in O(K) space.

    >>> for k in range(1, 11):
    ...     print(pascal_row(k))
    [1]
    [1, 1]
    [1, 2, 1]
    [1, 3, 3, 1]
    [1, 4, 6, 4, 1]
    [1, 5, 10, 10, 5, 1]
    [1, 6, 15, 20, 15, 6, 1]
    [1, 7, 21, 35, 35, 21, 7, 1]
    [1, 8, 28, 56, 70, 56, 28, 8, 1]
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
    """
    assert k > 0, 'K must be a positive integer.'

    if k == 1:
        return [1]
    
    res = [0] * k
    res[0], res[1] = 1, 1
    for i in range(2, k):
        res[i] = 1
        prev = res[0]
        for j in range(1, i):
            res[j], prev = res[j] + prev, res[j]
    return res