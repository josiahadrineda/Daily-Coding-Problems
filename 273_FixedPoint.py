def has_fixed_point(nums):
    """Given a list of integers NUMS, determines whether there exists a fixed point
    in NUMS, where a fixed point is defined as an element whose value is equal to
    its index.

    >>> has_fixed_point([-6, 0, 2, 40])
    True
    >>> has_fixed_point([1, 5, 7, 8])
    False
    """
    assert nums, 'NUMS cannot be an empty list.'

    for i,e in enumerate(nums):
        if i == e:
            return True
    return False