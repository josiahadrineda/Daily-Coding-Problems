def max_triangle_path(triangle):
    """Given a list of lists of integers, where each list corresponds to
    a row in a triangle of numbers TRIANGLE, returns the maximum "weight"
    of all paths from top to bottom of TRIANGLE.

    >>> triangle = [
    ...     [1],
    ...     [1, 1],
    ...     [1, 2, 1],
    ...     [1, 3, 3, 1],
    ...     [1, 4, 6, 4, 1]
    ... ]
    >>> max_triangle_path(triangle)
    13
    """
    assert triangle, 'TRIANGLE cannot be an empty list.'

    return sum([max(row) for row in triangle])