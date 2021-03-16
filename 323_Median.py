# https://github.com/vineetjohn/daily-coding-problem/blob/master/solutions/problem_323.py

"""
Comments:
 - This alg isn't guaranteed, but we can pretty reliably say that it returns the 'median'
 - We pick N // 2 numbers from a uniform distribution and return their median
 - Although this is still technically O(N), it is most definitely faster than standard
"""

from statistics import median
from random import randint
from heapq import heappush

def unstable_median(nums):
    """Given an unordered list of integers NUMS, computes the median in less than O(N)
    time. More precisely, finds an element whose rank is between N / 4 and 3 * N / 4
    (where N = len(NUMS)), with a high level of certainty.

    **Note: The rank of an element is defined as the distance between the element and
    the first element of the array when arranged in ascending order.**

    >>> nums = [1, 5, 2, 3, 6, 8, 7, 4, 3, 5, 2, 4, 7, 6, 8, 1]
    >>> iter = 100000
    >>> # Median of above NUMS = 4.5
    >>> 3 <= median([unstable_median(nums) for _ in range(iter)]) <= 6
    True
    """
    assert nums, 'NUMS cannot be an empty list.'

    n = len(nums)

    h = []
    for _ in range(n // 2):
        r = randint(0, n - 1)
        heappush(h, nums[r])
    return h[len(h) // 2]