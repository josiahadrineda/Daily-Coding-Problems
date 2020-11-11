def modulo_subset(nums):
    """Given a list of distinct positive integers NUMS, finds the largest subset
    such that every pair of elements in the subset (i, j) satisfies either
    i % j == 0 or j % i == 0.

    >>> sorted(modulo_subset([3, 5, 10, 20, 21]))
    [5, 10, 20]
    >>> sorted(modulo_subset([1, 3, 6, 24]))
    [1, 3, 6, 24]
    >>> sorted(modulo_subset([3, 9, 15, 30]))
    [3, 15, 30]
    >>> sorted(modulo_subset([1, 2, 3, 4, 5]))
    [1, 2, 4]
    """
    assert nums, 'NUMS cannot be an empty list.'

    return modulo_subset_backtrack(sorted(nums), [], [])

def modulo_subset_backtrack(nums, curr, res):
    for i in range(len(nums)):
        if not curr or nums[i] % curr[-1] == 0:
            curr.append(nums[i])
            res = modulo_subset_backtrack(nums[i+1:], curr, res)
            curr.pop()
    res = curr.copy() if len(curr) > len(res) else res
    return res