def sort(nums, k):
    """Given a list of integers NUMS where each integer is at most K positions
    away from its sorted position, sorts NUMS in O(NlogK) time.

    >>> sort([1, 0, 2, 4, 3], 2)
    [0, 1, 2, 3, 4]
    """
    assert nums, 'NUMS cannot be an empty list.'
    assert k > 0, 'K must be a positive integer.'

    for i in range(len(nums)):
        s, e = max(i - k + 1, 0), min(i + k, len(nums))
        sl, el = nums[:s], nums[e:]
        ml = sorted(nums[s:e])
        nums = sl + ml + el
    return nums