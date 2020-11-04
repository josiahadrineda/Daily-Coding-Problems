def nonoverlapping_intervals(intervals):
    """Given a list of intervals INTERVALS, determines the minimum
    number of intervals that must be removed to make the rest of
    the intervals non-overlapping.

    *Note: intervals can "touch" ([1, 2] and [2, 3]) and won't
    be considered non-overlapping.*

    >>> nonoverlapping_intervals([[2, 3], [2, 3], [2, 3]])
    2
    >>> nonoverlapping_intervals([[1, 2], [2, 4], [3, 4]])
    1
    >>> nonoverlapping_intervals([[1, 10], [1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
    1
    """
    assert intervals, 'INTERVALS must not be an empty list.'

    intervals.sort(key=lambda x: x[1])

    cnt, e = 1, intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] >= e:
            cnt, e = cnt + 1, intervals[i][1]
    return len(intervals) - cnt