def sunset(heights):
    """Given a list of building heights HEIGHTS, returns the number of buildings with
    an unobstructed view of the setting sun to the east (HEIGHTS[len(HEIGHTS)]).

    >>> sunset([3, 7, 8, 3, 6, 1])
    3
    """
    assert heights, 'HEIGHTS cannot be an empty list.'

    res, curr_max = 0, float('-inf')
    for i in range(len(heights) - 1, -1, -1):
        h = heights[i]
        if h >= curr_max:
            res += 1
            curr_max = h
    return res