from heapq import heappush, heappop

def lock_combo(target, dead_ends):
    """You are given a circular lock with three wheels, each of which display the
    numbers 0 - 9. In addition, the lock has a certain number of "dead ends" which
    freeze the lock if the lock is turned to one of them. Considering a "move" to be
    the rotation of a single wheel by one digit in either direction, computes the
    minimum number of moves required to reach the TARGET state (or None if TARGET)
    is impossible to reach.

    **Note: A combo is represented as a TUPLE of 3 integers (0 - 9).**

    >>> lock_combo((3, 4, 5), [(3, 4, 4)])
    12

    """
    assert target and len(target) == 3, 'TARGET must be a tuple of 3 integers (0 - 9).'
    assert dead_ends and all([len(de) == 3 for de in dead_ends]), 'All dead ends in DEAD_ENDS must be valid combos.'

    def distance(c1, c2):
        return sum([abs(x - y) for x,y in zip(c1, c2)])

    visited = set()
    q = []
    heappush(q, (distance((0, 0, 0), target), 0, (0, 0, 0)))
    while q:
        dist, moves, combo = heappop(q)
        if combo == target:
            return moves
        if combo not in visited:
            visited.add(combo)
            a, b, c = combo
            for new_combo in (a+1, b, c), (a-1, b, c), (a, b+1, c), (a, b-1, c), (a, b, c+1), (a, b, c-1):
                heappush(q, (distance(new_combo, target), moves + 1, new_combo))
    return None