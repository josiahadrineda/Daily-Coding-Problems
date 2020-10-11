from math import sqrt

def nearest_k_points(points, center, k):
    """Given a list of points POINTS, the central point CENTER, and
    a nonnegative integer K, returns the nearest K POINTS from CENTER.

    >>> nearest_k_points([(0, 0), (5, 4), (3, 1)], (1, 2), 2)
    [(0, 0), (3, 1)]
    """
    assert k >= 0, 'Cannot return a negative number of points.'
    assert center, 'No reference.'

    if not points or len(points) == 0:
        return []
    if k >= len(points):
        return points

    return sorted(points, key=distance(center))[:k]

def distance(center):
    cx, cy = center
    def find_distance(point):
        px, py = point
        diff_x, diff_y = px - cx, py - cy
        return sqrt(diff_x**2 + diff_y**2)
    return find_distance