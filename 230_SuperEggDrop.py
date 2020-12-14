def super_egg_drop(n, k):
    """Given N identical eggs and access to a building with K floors, determines
    the lowest floor that will cause an egg to break, if dropped from that floor.
    Assume that if an eggs breaks when dropped from the Xth floor, an egg will also
    break when fropped from any floor greater than X.

    >>> super_egg_drop(1, 5)
    5
    >>> super_egg_drop(2, 6)
    3
    >>> super_egg_drop(3, 14)
    4
    """
    assert n > 0, 'N must be a positive integer.'
    assert k > 0, 'K must be a positive integer.'

    # dp[i][j] = max moves given i floors and j eggs
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            # Use up a move, first dp = if egg breaks, second dp = if egg doesn't break
            dp[i][j] = 1 + dp[i - 1][j - 1] + dp[i - 1][j]
        # If the number of moves >= number of floors available, return the current floor,
        # as we can guarantee which floor is the valid floor given equal or ample moves
        if dp[i][j] >= k:
            return i