from bisect import bisect_left

def lis(nums):
    """Given a list of integers NUMS, computes the longest increasing subsequence (LIS)
    in O(N log N) time.

    >>> lis([10, 9, 2, 5, 3, 7, 101, 18])
    [2, 3, 7, 18]
    >>> lis([7, 7, 7, 7, 7, 7, 7])
    [7]
    >>> lis([5, 4, 3, 2, 1])
    [1]
    """
    assert nums, 'NUMS cannot be an empty list.'

    res = []
    for num in nums:
        if not res or res[-1] < num:
            res.append(num)
        else:
            i = bisect_left(res, num)
            res[i] = num
    return res