def smallest_integer_not_in_list(l):
    """Given a sorted list of positive integers L, returns the smallest positive integer
    that is not the sum of a subset of L.

    >>> smallest_integer_not_in_list([1, 2, 3, 10])
    7
    >>> smallest_integer_not_in_list([1, 2, 3, 4, 5, 7, 8, 9, 10])
    50
    """
    assert l, 'L cannot be an empty list.'
    assert all([n > 0 for n in l]), 'L must only contain positive integers.'

    res = 1
    for n in l:
        if n > res:
            break
        res += n
    return res