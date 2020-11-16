def minimum_element(nums):
    """Given a list of integers NUMS (sorted in ascending order and rotated 
    at some unknown pivot), finds the minimum element in O(log N) time.

    **Note: All elements in nums are unique.**

    >>> minimum_element([5, 7, 10, 3, 4])
    3
    >>> minimum_element([3, 4, 5, 7, 10])
    3
    """
    assert nums, 'NUMS cannot be an empty list.'

    l, r = 0, len(nums) - 1
    while l <= r:
        m = l + (r - l) // 2
        if nums[m] > nums[(m+1) % len(nums)]:
            return nums[(m+1) % len(nums)]
        elif nums[m] >= nums[0]:
            l = m + 1
        else:
            r = m - 1
    return l