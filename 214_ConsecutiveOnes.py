def consecutive_ones(n):
    """Given a positive integer N, returns the length of the longest consecutive
    run of ones in its binary representation.

    >>> consecutive_ones(156)
    3
    """
    assert n > 0, 'N must be a positive integer.'

    bin_n = str(bin(n))[2:]
    
    max_streak, streak = 0, 0
    for digit in bin_n:
        if digit == '1':
            streak += 1
        else:
            max_streak = max(max_streak, streak)
            streak = 0
    return max(max_streak, streak)