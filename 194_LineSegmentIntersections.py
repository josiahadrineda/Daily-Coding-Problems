def line_segment_intersections(ps, qs):
    """Given two lists of n points, one list p1, p2, ..., pn (Ps) on the line
    y = 0 and the other list q1, q2, ..., qn (Qs) on the line y = 1, determines
    the number of pairs of line segments that intersect - where each line segment
    is drawn from pi to qi.

    >>> line_segment_intersections([1, 2, 3, 4, 5], [2, 3, 4, 5, 6])
    0
    >>> line_segment_intersections([1, 2, 4, 3, 5], [2, 4, 3, 6, 5])
    3
    """
    assert ps, 'Ps cannot be an empty list.'
    assert qs, 'Qs cannot be an empty list.'

    cnt = 0
    for i in range(len(ps)):
        ref_p, ref_q = ps[i], qs[i]
        for j in range(i):
            p, q = ps[j], qs[j]
            if p < ref_p and q > ref_q:
                cnt += 1
            elif p > ref_p and q < ref_q:
                cnt += 1
    return cnt