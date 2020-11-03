def max_subarray_sum_circular(nums):
    """Given an circular array of integers NUMS, computes the maximum
    sum of a subarray included within NUMS.

    >>> max_subarray_sum_circular([])
    0
    >>> max_subarray_sum_circular([8, -1, 3, 4])
    15
    >>> max_subarray_sum_circular([-4, 5, 1, 0])
    6
    """
    
    try:
        global_max, global_min, local_max, local_min = 0, 0, nums[0], nums[0]
    except IndexError:
        return 0

    tot = nums[0]
    for i in range(1, len(nums)):
        num = nums[i]
        tot += num
        local_max, local_min = max(local_max + num, num), min(local_min + num, num)
        global_max, global_min = max(global_max, local_max), min(global_min, local_min)
    return max(global_max, tot - global_min)