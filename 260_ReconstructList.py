from operator import lt, gt

def reconstruct(clues):
    """A list of integers 0...N is shuffled. Given a list of clues CLUES, where clues[i]
    is either None, '+', or '-' (indicating N/A, bigger number than clues[i-1], and
    smaller number than clues[i-1]), reconstructs a possible orientation for the list.

    **Note: Assume that a valid sequence can be found from CLUES.**

    >>> reconstruct([None, '+', '+', '-', '+'])
    [0, 1, 3, 2, 4]
    """
    assert clues, 'CLUES cannot be an empty list.'

    COMPARISONS = {'-': lt, '+': gt}

    def reconstruct_backtrack(nums, clues, ind, curr):
        if not nums:
            return curr
        elif not ind:
            for i, num in enumerate(list(nums)):
                nums.remove(num)
                res = reconstruct_backtrack(nums, clues, ind + 1, curr + [num])
                if res:
                    return res
                nums.insert(i, num)
        else:
            clue = COMPARISONS[clues[ind]]
            for i, num in enumerate(valid_nums(nums, clue, curr[-1])):
                nums.remove(num)
                res = reconstruct_backtrack(nums, clues, ind + 1, curr + [num])
                if res:
                    return res
                nums.insert(i, num)
            return []

    def valid_nums(nums, clue, prev):
        res = []
        for num in nums:
            if clue(num, prev):
                res.append(num)
        return res

    nums = list(range(len(clues)))
    return reconstruct_backtrack(nums, clues, 0, [])