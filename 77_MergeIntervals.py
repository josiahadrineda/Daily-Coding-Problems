def merge_intervals(intervals):
    if not intervals:
        return []
    elif len(intervals) <= 1:
        return intervals

    intervals.sort()
    i = 1
    while i < len(intervals):
        if intervals[i-1][0] <= intervals[i][0] <= intervals[i-1][1] and intervals[i][1] >= intervals[i-1][1]:
            intervals[i-1] = (intervals[i-1][0], intervals[i][1])
            intervals.remove(intervals[i])
        elif intervals[i][1] < intervals[i-1][1]:
            intervals.remove(intervals[i])
        else:
             i += 1
    return intervals 

assert merge_intervals([(1,3),(5,8),(4,10),(20,25)]) == [(1,3),(4,10),(20,25)]
assert merge_intervals([(1,3),(2,4),(5,7),(6,8)]) == [(1,4),(5,8)]
assert merge_intervals([(1,2),(9,10),(15,16)]) == [(1,2),(9,10),(15,16)]
assert merge_intervals([]) == []