def largest_integer(nums):
    """Given a list of positive integers NUMS, rearranges NUMS so as to form
    the largest possible integer.

    >>> largest_integer([10, 7, 76, 415])
    77641510
    """
    def largest_integer_backtrack(nums, curr):
        nonlocal res
        if not nums:
            a = int(curr)
            b = int(res) if res else 0
            if a > b:
                res = curr
        else:
            for i in range(len(nums)):
                largest_integer_backtrack(nums[:i] + nums[i+1:], curr + str(nums[i]))
    
    res = ''
    largest_integer_backtrack(nums, '')
    return int(res)