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

    def max_triangle_path_recur(triangle, row, index, curr):
        if row == len(triangle):
            return curr
        else:
            l_index, r_index = index, index + 1
            return max(
                max_triangle_path_recur(triangle, row + 1, l_index, curr + [triangle[row][index]]),
                max_triangle_path_recur(triangle, row + 1, r_index, curr + [triangle[row][index]])
            )

    return sum(max_triangle_path_recur(triangle, 0, 0, []))