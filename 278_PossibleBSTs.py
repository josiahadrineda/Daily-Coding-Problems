def possible_bsts(n):
    """Given a positive integer N representing the number of nodes labeled 1 ... N,
    returns the number of possible BSTs one can construct.

    >>> possible_bsts(3)
    5
    >>> possible_bsts(19)
    1767263190
    """
    assert n > 0, 'N must be a positive integer.'

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, n + 1):
        cnt = 0
        for j in range(1, i + 1):
            cnt += dp[j - 1] * dp[i - j]
        dp[i] = cnt
    return dp[-1]