def list_permutation(l, perm):
    """A permutation can be specified by an list L, where L[i] represents
    the location of the element at i in the permutation. For example, [2, 1, 0]
    represents the permutation where elements at the index o and 2 are swapped.
    
    Given a list L and a permutation PERM, applies PERM to L.

    >>> list_permutation(['a', 'b', 'c'], [2, 1, 0])
    ['c', 'b', 'a']
    """
    assert l, 'L cannot be an empty list.'
    assert max(perm) == len(l) - 1, 'Incorrect formatting of L and PERM.'

    res = []
    for p in perm:
        res.append(l[p])
    return res