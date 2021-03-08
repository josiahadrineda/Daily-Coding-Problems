def is_toeplitz(matrix):
    """Given a matrix of integers MATRIX, determines whether or not MATRIX is a
    Toeplitz matrix, where each diagonal from top left to bottom right contains the
    same elements.

    >>> matrix = [
    ...     [1, 2, 3, 4, 8],
    ...     [5, 1, 2, 3, 4],
    ...     [4, 5, 1, 2, 3],
    ...     [7, 4, 5, 1, 2]
    ... ]
    >>> is_toeplitz(matrix)
    True
    >>> matrix[0][0] = 2
    >>> is_toeplitz(matrix)
    False
    """
    assert matrix, 'MATRIX cannot be an empty list.'

    prev = None
    for row in matrix:
        all_but_first, all_but_last = row[1:], row[:-1]
        if prev and prev != all_but_first:
            return False
        prev = all_but_last
    return True