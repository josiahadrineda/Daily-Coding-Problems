def rotate(l, K):
    """
    Given a list l, rotate said list by K elements.

    >>> rotate([1, 2, 3, 4, 5, 6], 2)
    [3, 4, 5, 6, 1, 2]
    """
    assert l, 'Cannot rotate empty list.'
    assert K < len(l), 'K is out of bounds.'

    K %= len(l)
    if K == 0:
        return l
    
    l.reverse()
    K = len(l) - K
    l[:K], l[K:] = reversed(l[:K]), reversed(l[K:])
    return l