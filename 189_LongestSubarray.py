def longest_subarray(nums):
    """Given an array of elements NUMS, returns the length of the longest
    subarray where all its elements are distinct.

    >>> longest_subarray([5, 1, 3, 5, 2, 3, 4, 1])
    5
    >>> longest_subarray([1, 1, 2, 2, 3, 3, 4, 4, 5, 5])
    2
    >>> longest_subarray([2, 2, 2, 2, 2])
    1
    """
    assert nums, 'NUMS cannot be an empty list.'

    dp = [1] * len(nums)
    visited = set()
    j = 0
    for i, num in enumerate(nums):
        if not visited:
            visited.add(num)
        elif num not in visited:
            visited.add(num)
            dp[i] = dp[i - 1] + 1
        else:
            while j < len(nums) and nums[j] != num:
                if nums[j] in visited:
                    visited.remove(nums[j])
                j += 1
            j += 1
            dp[i] = len(visited)
    return max(dp)