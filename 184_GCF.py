def greatest_common_factor(nums):
    """Given a list of nonnegative integers NUMS, computes the GCF between them.

    >>> greatest_common_factor([42, 56, 14])
    14
    >>> greatest_common_factor([42, 56, 15])
    1
    """
    assert nums, 'NUMS cannot be an empty list.'
    for num in nums:
        assert isinstance(num, int), 'Num in NUMS must be an integer.'
        assert num > 0, 'Num in NUMS mus be nonnegative.'

    for i in range(min(nums), 0, -1):
        if all(map(lambda x: x % i == 0, nums)):
            return i