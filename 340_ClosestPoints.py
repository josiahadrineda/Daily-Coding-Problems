from math import sqrt

def distance(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return sqrt((x1 - x2)**2 + (y1 - y2)**2)

# TC: O(N^2), SC: O(1)
def closest_points(points):
    """Given a list of points (x, y) on a 2D Cartesian plane POINTS, finds the two
    closest points.

    >>> closest_points([(1, 1), (-1, -1), (3, 4), (-4, -3), (-1, -6), (1, 6)])
    [(1, 1), (-1, -1)]
    """
    assert len(points) >= 2, 'There are not enough points in POINTS to compare.'

    res, min_dist = None, float('inf')
    for i, p1 in enumerate(points):
        for p2 in points[i + 1:]:
            dist = distance(p1, p2)
            if dist < min_dist:
                res = [p1, p2]
                min_dist = dist
    return res

# TC: O(NlogN), SC: O(N)
# https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer-algorithm/
def closest_points_quick(points):
    """Same objective as above brute-force algorithm, only faster.

    >>> closest_points([(1, 1), (-1, -1), (3, 4), (-4, -3), (-1, -6), (1, 6)])
    [(1, 1), (-1, -1)]
    """
    assert len(points) >= 2, 'There are not enough points in POINTS to compare.'

    def closest_recur(points, n):
        if n <= 3:
            return -1, closest_points(points)

        m = n // 2
        mp = points[m]

        min_dist_points_l = closest_recur(points[:m], m)
        min_dist_points_r = closest_recur(point[m:], n - m)
        min_dist_points_sides = min(
            min_dist_points_l,
            min_dist_points_r,
            key=lambda mdp: mdp[0]
        )
        min_dist_sides, _ = min_dist_points_sides

        strip = [p for p in sort_y if abs(mp[0] - p[0]) < min_dist_sides]
        return min(
            min_dist_points_sides,
            closest_strip(strip, min_dist_points_sides),
            key=lambda mdp: mdp[0]
        )

    # Proven to run in O(N) as opposed to O(N^2)
    # http://people.csail.mit.edu/indyk/6.838-old/handouts/lec17.pdf
    def closest_strip(strip, dist_points):
        min_dist, min_points = dist_points
        for i,p1 in enumerate(strip):
            for p2 in strip[i + 1:]:
                if p2[1] - p1[1] >= min_dist:
                    break
                min_dist = distance(p1, p2)
                min_points = [p1, p2]
        return min_dist, min_points

    sort_x = sorted(points, key=lambda p: p[0])
    sort_y = sorted(points, key=lambda p: p[1])
    min_dist, min_points = closest_recur(sort_x, len(sort_x))
    return min_points