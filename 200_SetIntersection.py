def set_intersection(intervals):
    """Given a set of intervals on the real line INTERVALS, computes the smallest
    set of points P such that every interval in INTERVALS contains at least one
    point in P.

    >>> set_intersection([(1, 4), (4, 5), (7, 9), (9, 12)])
    [4, 9]
    >>> set_intersection([(1, 4), (-2, 6), (4, 5), (7, 9), (9, 12)])
    [4, 9]
    >>> set_intersection([(1, 4), (-2, 0), (4, 5), (7, 9)])
    [0, 7]
    """
    assert intervals, 'INTERVALS cannot be an empty list.'

    starts, ends = [s for s,_ in intervals], [e for _,e in intervals]
    return [min(ends), max(starts)]