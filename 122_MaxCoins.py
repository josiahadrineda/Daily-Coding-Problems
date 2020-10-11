def max_coins(matrix):
    """
    Given a 2D matrix where each cell represents the
    number of coins in that cell, finds the maximum
    number of coins you can collect from the top left
    corner to the bottom right corner, moving only
    right and down.

    >>> matrix = [[0,3,1,1],[2,0,0,4],[1,5,3,1]]
    >>> max_coins(matrix)
    12
    """
    assert matrix, 'Cannot find maximum coins with an empty matrix.'

    m, n = len(matrix), len(matrix[0])

    dp = [[0] * n for _ in range(m)]
    dp[0][0] = matrix[0][0]

    for i in range(1, m):
        # first column
        dp[i][0] = dp[i-1][0] + matrix[i][0]

    for i in range(1, n):
        # first row
        dp[0][i] = dp[0][i-1] + matrix[0][i]

    # dp through the rest of the matrix
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matrix[i][j]

    return dp[-1][-1]