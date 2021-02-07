def skyline(buildings):
    """The skyline of a city is composed of several buildings of various widths and
    heights, possibly overlapping one another when viewed from a distance. Each
    building in BUILDINGS is represented by (left, right, height) tuples, which
    describes where where on an imaginary x-axis said building begins and ends, as
    well as how tall it is. Given a list of buildings BUILDINGS, returns the skyline
    as a list of (x, height) tuples, giving the locations at which the height visible
    to a distant observer changes, in addition to each new height.

    >>> skyline([(0, 15, 3), (4, 11, 5), (19, 23, 4)])
    [(0, 3), (4, 5), (11, 3), (15, 0), (19, 4), (23, 0)]
    """
    assert buildings, 'BUILDINGS cannot be an empty list.'

    def compare(point_a, point_b):
        x_a, h_a, q_a = point_a
        x_b, h_b, q_b = point_b
        if x_a == x_b:
            if q_a == q_b == 's':
                if h_a >= h_b:
                    return point_a
                return point_b
            elif q_a == q_b == 'e':
                if h_a <= h_b:
                    return point_a
                return point_b
            else:
                if h_a >= h_b:
                    return point_a
                return point_b
        return point_a

    points = []
    for b in buildings:
        s, e, h = b
        points.append((s, h, 's'))
        points.append((e, h, 'e'))
    points.sort(key=lambda x: x[0])

    res, pq = [], set([0])
    max_h = 0
    while len(points) > 1:
        point_a, point_b = points[0], points[1]
        p = compare(point_a, point_b)
        points.remove(p)
        
        x, h, q = p
        if q == 's':
            pq.add(h)
            if h > max_h:
                max_h = h
                res.append((x, h))
        else:
            pq.remove(h)
            max_pq = max(pq)
            if max_pq != max_h:
                max_h = max_pq
                res.append((x, max_h))
    res.append((points[0][0], 0))
    return res