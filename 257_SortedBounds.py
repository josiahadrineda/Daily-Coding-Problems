def sorted_bounds(nums):
    """Given an unsorted list of integers NUMS, returns the bounds of the
    smallest window that must be sorted in order for the entire list to be sorted.
    
    >>> sorted_bounds([3, 7, 5, 6, 9])  # [7, 5, 6] -> [5, 6, 7]
    (1, 3)
    >>> sorted_bounds([5, 4, 3, 2, 1])
    (0, 4)
    """
    assert nums, 'NUMS cannot be an empty list.'

    sorted_nums = sorted(nums)
    i, j = float('inf'), float('-inf')
    for k, (c1, c2) in enumerate(zip(nums, sorted_nums)):
        if c1 != c2:
            i, j = min(i, k), max(j, k)
    return (i, j)