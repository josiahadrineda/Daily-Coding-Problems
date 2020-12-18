def min_max(nums):
    """Given a list of numbers NUMS of length N, finds both the minimum and maximum
    using less than 2 * (N - 2) comparisons.

    >>> min, max = min_max([4, 3, 1, 2, 5])
    >>> min
    1
    >>> max
    5
    """
    assert nums, 'NUMS cannot be an empty list.'

    """
    # 2N comparisons
    return min(nums), max(nums)

    # 2 * (N - 1) comparisons
    min_num, max_num = nums[0], nums[0]
    for num in nums[1:]:
        min_num, max_num = min(min_num, num), max(max_num, num)
    return min_num, max_num

    # <= 2 * (N - 2) + 1 comparisons
    if len(nums) == 1:
        return nums[0], nums[0]
    
    if nums[0] < nums[1]:
        min_num, max_num = nums[0], nums[1]
    else:
        min_num, max_num = nums[1], nums[0]
    
    for num in nums[2:]:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num
    return min_num, max_num
    """

    # 5 / 4N comparisons (Tournament Style)
    if len(nums) == 1:
        return nums[0], nums[0]

    def split_min_max(nums):
        mins, maxes = [], []
        i = 0
        while i < len(nums):
            if i == len(nums) - 1:
                mins.append(nums[i])
                maxes.append(nums[i])
            else:
                if nums[i] < nums[i + 1]:
                    mins.append(nums[i])
                    maxes.append(nums[i + 1])
            i += 2
        return mins, maxes

    mins, maxes = split_min_max(nums)
    while len(mins) > 1 and len(maxes) > 1:
        mins, _ = split_min_max(mins)
        _, maxes = split_min_max(maxes)
    return mins[0], maxes[0]