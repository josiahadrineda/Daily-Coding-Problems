def shortest_route(elevations, paths):
    """A competitive runner would like to create a route that starts and ends at his
    house (0), with the condition that the route goes entirely uphill at first, and
    then entirely downhill. Given a dictionary of places ELEVATIONS of the form
    {location: elevation}, and a dictionary mapping paths between some of these
    locations to their corresponding distances PATHS, finds the length of the shortest
    route satisfying the condition above.

    **Note: The locations are labeled from 1...N.**

    >>> elevations = {
    ...     0: 5,
    ...     1: 25,
    ...     2: 15,
    ...     3: 20,
    ...     4: 10
    ... }
    >>> paths = {
    ...     (0, 1): 10,
    ...     (0, 2): 8,
    ...     (0, 3): 15,
    ...     (1, 3): 12,
    ...     (2, 4): 10,
    ...     (3, 0): 17,
    ...     (3, 4): 5,
    ...     (4, 0): 10
    ... }
    >>> shortest_route(elevations, paths)
    28
    """
    assert elevations, 'ELEVATIONS cannot be an empty dictionary.'
    assert paths, 'PATHS cannot be an empty dictionary.'

    def is_valid(se, ee, dir):
        if dir == 'inc':
            if ee > se:
                return 'inc'
            elif ee < se:
                return 'dec'
        elif dir == 'dec':
            if ee > se:
                return ''
            elif ee < se:
                return 'dec'

    es = elevations
    ps = {}
    for (s, e), dist in paths.items():
        if ps.get(s) == None:
            ps[s] = []
        ps[s].append((e, dist))

    q = []
    for (e, dist) in ps[0]:
        if es[e] > es[0]:
            q.append((e, dist, 'inc'))

    res = float('inf')
    while q:
        s, dist, dir = q.pop(0)
        if s == 0:
            res = min(res, dist)
            continue
        
        for e, new_dist in ps[s]:
            new_dir = is_valid(es[s], es[e], dir)
            if new_dir:
                q.append((e, dist + new_dist, new_dir))
    return res