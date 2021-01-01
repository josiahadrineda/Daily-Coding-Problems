# You can also solve this using a Trie to make TC O(N), but I'll leave that for another time.

def max_xor(nums):
    """Given a list of integers NUMS, computes the maximum
    XOR of any two elements in NUMS.

    >>> max_xor([1, 2, 3, 4])
    7
    """
    assert nums, 'NUMS cannot be an empty list.'
    assert len(nums) > 1, 'Cannot compute the max XOR of only one element.'

    res = float('-inf')
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            res = max(res, nums[i] ^ nums[j])
    return res