# Copied from 185_AreaOfIntersection.py
def area_of_intersection(rect1, rect2):
    A, B = rect1["top_left"]
    C, D = A + rect1["dimensions"][0], B - rect1["dimensions"][1]

    E, F = rect2["top_left"]
    G, H = E + rect2["dimensions"][0], F - rect2["dimensions"][1]

    p1 = (max(A, E), min(B, F))
    p2 = (min(C, G), max(D, H))

    if p1[0] > p2[0] or p2[1] > p1[1]:
        return 0
    else:
        width = p2[0] - p1[0]
        height = p1[1] - p2[1]
        return width * height

def rectangle_overlap(rects):
    """Given a list of rectangles RECTS (format implemented below), returns
    whether any of them overlap. One rectangle completely covering another rectangle
    is also considered overlap.

    >>> rects = [
    ...     {
    ...         "top_left": (1, 4),
    ...         "dimensions": (3, 3) # idth, height
    ...     },
    ...     {
    ...         "top_left": (-1, 3),
    ...         "dimensions": (2, 1)
    ...     },
    ...     {
    ...         "top_left": (0, 5),
    ...         "dimensions": (4, 3)
    ...     }
    ... ]
    >>> rectangle_overlap(rects)
    True
    >>> rects[-1]["top_left"] = (100, 100)
    >>> rectangle_overlap(rects)
    False
    """
    assert rects, 'RECTS cannot be an empty list.'

    for i in range(len(rects) - 1):
        rect_A = rects[i]
        for j in range(i + 1, len(rects)):
            rect_B = rects[j]
            if area_of_intersection(rect_A, rect_B):
                return True
    return False