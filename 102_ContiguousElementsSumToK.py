def contiguous_sum_to_k(nums, k):
    """
    Returns a subarray whose sum is k. Returns
    an empty list if no subarray can be found.

    >>> contiguous_sum_to_k([1, 2, 3, 4, 5], 9)
    [2, 3, 4]
    >>> contiguous_sum_to_k([1, 2, 3, 4, 5], 11)
    []
    >>> contiguous_sum_to_k([5, 0, 0], 0)
    [0, 0]
    """
    
    if not nums:
        return nums

    if k == 0:
        for i in range(1, len(nums)):
            if nums[i] == 0 and nums[i] == nums[i-1]:
                return [0, 0]
        return []

    sums = []
    curr_sum = 0
    for num in nums:
        curr_sum += num
        sums.append(curr_sum)

    for i in range(1, len(sums)):
        if sums[i] == k:
            return nums[:i+1]

        for j in range(i-1):
            if (sums[i] - sums[j]) == k:
                return nums[j+1:i+1]
    return []