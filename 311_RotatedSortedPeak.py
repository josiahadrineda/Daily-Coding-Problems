def rotated_sorted_peak(nums):
    """Given a sorted, rotated list of integers NUMS, where each integer in NUMS is
    distinct, finds the "peak" element in O(log N) time.

    >>> nums = list(range(1, 11))
    >>> for i in range(len(nums)):
    ...     rotated_nums = nums[i:] + nums[:i]
    ...     assert rotated_sorted_peak(rotated_nums) == 10
    """
    assert nums, 'NUMS cannot be an empty list.'

    first, last = nums[0], nums[-1]
    if first < last:
        return last

    l, r = 0, len(nums) - 1
    while l < r:
        m = l + (r - l) // 2
        num = nums[m]
        if first <= num >= last:
            num2 = nums[m + 1]
            if num > num2:
                return num
            l = m + 1
        elif num <= last:
            r = m - 1
    return nums[l]