# https://www.geeksforgeeks.org/how-to-check-if-a-given-point-lies-inside-a-polygon/

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __key(self):
        return (self.x, self.y)

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

def inside(points, point):
    """Given a list of Points POINTS that, when connected with line segments forms a
    polygon (you may also assume that these points are ordered in that manner),
    determines whether or not a Point POINT lies within the polygon. A point that
    lies on the border of the polygon is NOT considered inside.

    **Note: The format of a Point is (x, y)**

    >>> diamond = [Point(1, 0), Point(0, 1), Point(1, 2), Point(2, 1)]
    >>> inside(diamond, Point(1, 1))
    True
    >>> inside(diamond, Point(1, 1.5))
    True
    >>> inside(diamond, Point(0.5, 0.5))
    False
    >>> inside(diamond, Point(1, 0))
    False
    >>> inside(diamond, Point(100, 100))
    False
    """
    assert points, 'POINTS cannot be an empty list.'
    assert len(points) >= 3, 'Cannot construct a polygon with less than three Points.'

    n = len(points)
    points_of_intersection = set()
    ext = Point((1 << 31) - 1, point.y)
    for i in range(n):
        p1, p2 = points[i], points[(i + 1) % n]
        if lines_intersect(p1, p2, point, ext):
            # Check for collinearity
            if not orientation(p1, point, p2):
                # Indicates that POINT is on the border
                if inside_line(p1, p2, point):
                    return False
            points_of_intersection.add(point_of_intersection(p1, p2, point, ext))
    return len(points_of_intersection) % 2 == 1

def orientation(p, q, r):
    """0 -> collinear, 1 -> clockwise, -1 -> conterclockwise
    """
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if not val:
        return val
    return 1 if val > 0 else -1

def inside_line(p1, p2, q):
    return min(p1.x, p2.x) <= q.x <= max(p1.x, p2.x) and \
        min(p1.y, p2.y) <= q.y <= max(p1.y, p2.y)

def lines_intersect(p1, p2, q1, q2):
    o1 = orientation(p1, p2, q1)
    o2 = orientation(p1, p2, q2)
    o3 = orientation(q1, q2, p1)
    o4 = orientation(q1, q2, p2)

    if o1 != o2 and o3 != o4:
        return True
    elif not o1 and inside_line(p1, p2, q1):
        return True
    elif not o2 and inside_line(p1, p2, q2):
        return True
    elif not o3 and inside_line(q1, q2, p1):
        return True
    elif not o4 and inside_line(q1, q2, p2):
        return True
    return False

# https://stackoverflow.com/questions/20677795/how-do-i-compute-the-intersection-point-of-two-lines
def point_of_intersection(p1, p2, q1, q2):
    def det(a, b):
        return a.x * b.y - a.y * b.x
    
    xdiff = Point(p1.x - p2.x, q1.x - q2.x)
    ydiff = Point(p1.y - p2.y, q1.y - q2.y)

    div = det(xdiff, ydiff)
    d = Point(det(p1, p2), det(q1, q2))
    
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return Point(x, y)