def domitrominoes(n):
    """Given an empty 2xN board, where N is a positive integer, determines the total
    number of ways one can completely fill the board with dominoes
    
    >>> for i in range(1, 11):
    ...     print(domitrominoes(i))
    1
    2
    5
    11
    24
    53
    117
    258
    569
    1255
    """
    assert n > 0, 'N must be a positive integer.'

    dp = [0] * (n + 3)
    dp[0], dp[2] = -1, 1
    for i in range(n):
        dp[i + 3] = dp[i + 2] * 2 + dp[i]
    return dp[-1]