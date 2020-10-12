# https://leetcode.com/problems/rotate-image/discuss/18884/Seven-Short-Solutions-(1-to-7-lines)

def rotate_clockwise(matrix):
    """Given an N by N MATRIX, rotates it by 90 degrees clockwise.

    >>> matrix = [
    ...     [1, 2, 3],
    ...     [4, 5, 6],
    ...     [7, 8, 9]
    ... ]
    >>> rotate_clockwise(matrix)
    >>> matrix
    [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    """
    assert matrix, 'Input MATRIX must be valid.'
    assert len(matrix) == len(matrix[0]), 'MATRIX must be in the shape (N, N).'

    n = len(matrix)
    for r in range(n // 2):
        for c in range(n - n // 2):
            # Didn't know that ~ could be used to get 'reflection'!
            matrix[r][c], matrix[~c][r], matrix[~r][~c], matrix[c][~r] = \
                matrix[~c][r], matrix[~r][~c], matrix[c][~r], matrix[r][c]