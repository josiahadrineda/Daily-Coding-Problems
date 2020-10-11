def intersection(intervals):
    """
    Given a set of closed intervals, finds the smallest
    set of numbers that convers all the intervals.

    >>> intersection([[0, 3]])
    {0}
    >>> intersection([[0, 3], [2, 6]])
    {2}
    >>> intersection([[0, 3], [2, 6], [3, 4]])
    {3}
    >>> intersection([[0, 3], [2, 6], [3, 4], [6, 9]])
    {3, 6}
    """
    assert intervals, 'Cannot find intersection with zero intervals.'

    if len(intervals) == 1:
        return {intervals[0][0]}

    starts, ends = [x[0] for x in intervals], [x[1] for x in intervals]
    lb, ub = min(ends), max(starts)
    if len(intervals) == 2:
        # Note that we may have to switch bounds here
        lb, ub = min(lb, ub), max(lb, ub)
        i1, i2 = intervals[0], intervals[1]
        r1, r2 = range(i1[0], i1[1] + 1), range(i2[0], i2[1])
        for x in range(lb, ub + 1):
            if x in r1 and x in r2:
                return {x}
    return {lb, ub}