def min_bricks(bricks):
    """Given lengths of each brick for each row in a wall of bricks, returns the
    minimum number of bricks that must be cut to make a straight line.

    >>> bricks = [
    ...     [3, 5, 1, 1],
    ...     [2, 3, 3, 2],
    ...     [5, 5],
    ...     [4, 4, 2],
    ...     [1, 3, 3, 3],
    ...     [1, 1, 6, 1, 1]
    ... ]
    >>> min_bricks(bricks)
    2
    >>> min_bricks([[2, 1], [1, 2]])
    1
    >>> min_bricks([[1, 2], [1, 2]])
    0
    """
    assert bricks, 'BRICKS cannot be an empty list.'

    sum_freqs = {}
    for row in bricks:
        tot = 0
        for brick in row[:-1]:
            tot += brick
            if sum_freqs.get(tot) == None:
                sum_freqs[tot] = 0
            sum_freqs[tot] += 1
    return len(bricks) - max(sum_freqs.values())