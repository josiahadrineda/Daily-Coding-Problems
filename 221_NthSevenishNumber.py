def nth_sevenish_number(n):
    """Given a positive integer N, computes the Nth "sevenish" number, where
    a "sevenish" number is defined as a number that is either a power of 7 or
    the sum of unique powers of 7.

    >>> [nth_sevenish_number(i) for i in range(1, 11)]
    [1, 7, 8, 49, 50, 56, 57, 343, 344, 350]
    """
    assert n > 0, 'N must be a positive integer.'

    sevenish_nums, exp, i, j = [], 0, 0, 0
    while n:
        if not sevenish_nums or i == j:
            sevenish_nums.append(7**exp)
            exp, i, j = exp + 1, 0, len(sevenish_nums) - 1
        else:
            sevenish_nums.append(sevenish_nums[i] + sevenish_nums[j])
            i += 1
        n -= 1
    return sevenish_nums[-1]