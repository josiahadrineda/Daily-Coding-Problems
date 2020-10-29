def area_of_intersection(rect1, rect2):
    """Given two dictionaries representing two rectangles RECT1 and RECT2 (format is implemented below),
    returns the area of their intersection. If the two rectangles don't intersect, returns 0.

    >>> rect1 = {
    ...     "top_left": (1, 4),
    ...     "dimensions": (3, 3)
    ... }
    >>> rect2 = {
    ...     "top_left": (0, 5),
    ...     "dimensions": (4, 3)
    ... }
    >>> area_of_intersection(rect1, rect2)
    6
    >>> rect2["top_left"] = (100, 100)
    >>> area_of_intersection(rect1, rect2)
    0
    """
    assert isinstance(rect1, dict), 'RECT1 must be in dictionary format.'
    assert isinstance(rect2, dict), 'RECT2 must be in dictionary format.'

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