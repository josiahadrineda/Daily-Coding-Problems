def duplicate_element(nums):
    """Given an array of numbers NUMS whose elements belong to the set
    {1, 2, ..., n}, find the duplicate element in linear time and space.

    >>> duplicate_element([1, 2, 3, 4, 5, 5, 6, 7, 8, 9])
    5
    >>> duplicate_element([6, 2, 4, 1, 3, 2, 5, 2])
    2
    >>> duplicate_element([2, 2, 1, 2, 2])
    2
    """
    assert nums, 'Cannot find duplicate element in empty list.'

    slow, fast = nums[0], nums[0]
    while True:
        slow, fast = nums[slow], nums[nums[fast]]
        if slow == fast: break

    slow = nums[0]
    while slow != fast:
        slow, fast = nums[slow], nums[fast]
    return slow