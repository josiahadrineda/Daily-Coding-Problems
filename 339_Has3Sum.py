def has_three_sum(nums, k):
    """Given a list of integers NUMS, determines whether or not there are three
    integers in nums that sum up to integer K.

    >>> has_three_sum([20, 303, 3, 4, 25], 49)
    True
    >>> has_three_sum([-2, -1, 0, 1, 2], 0)
    True
    >>> has_three_sum([121, 232, 343, 454, 565], 82)
    False
    """
    assert nums, 'NUMS cannot be an empty list.'

    def has_two_sum(nums, k):
        addends = set()
        for num in nums:
            if k - num in addends:
                return True
            addends.add(num)
        return False

    if len(nums) < 3:
        return False

    for i, num in enumerate(nums):
        if has_two_sum(nums[:i] + nums[i + 1:], k - num):
            return True
    return False