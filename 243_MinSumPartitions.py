# More efficient method would be to use binary search.

from functools import lru_cache

def min_sum_partitions(nums, k):
    """Given a list of numbers NUMS and a positive integer K, splits
    NUMS into K partitions such that the maximum sum of any partition
    is minimized.

    **Note**: The max of the minimum sums should be returned.

    >>> min_sum_partitions([1, 2, 3, 4], 1) # [[1, 2, 3, 4]]
    10
    >>> min_sum_partitions([1, 2, 3, 4], 2) # [[1, 2, 3], [4]]
    6
    >>> min_sum_partitions([1, 2, 3, 4], 3) # [[1, 2], [3], [4]]
    4
    >>> min_sum_partitions([1, 2, 3, 4], 4) # [[1], [2], [3], [4]]
    4
    >>> min_sum_partitions([5, 1, 2, 7, 3, 4], 3) # [[5, 1, 2], [7], [3, 4]]
    8
    """
    assert nums, 'NUMS cannot be an empty list.'
    assert k > 0, 'K must be a positive integer.'
    assert len(nums) >= k, 'Cannot split NUMS into K partitions.'

    @lru_cache(maxsize=None)
    def min_sum_partitions_recur(i, k, currs):
        if k == 1:
            return max(sum(nums[i:]) + currs[0], currs[1])
        elif i == len(nums):
            return float('inf')
        else:
            part = float('inf')
            if currs[0]:
                part = min_sum_partitions_recur(i + 1, k - 1, (nums[i], max(currs[0], currs[1])))
            add_one = min_sum_partitions_recur(i + 1, k, (currs[0] + nums[i], currs[1]))
            return min(add_one, part)

    return min_sum_partitions_recur(0, k, (0, 0))