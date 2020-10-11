def number_of_paths(matrix):
    """Given a MATRIX of 0s and 1s, returns the number of ways
    one can traverse from the top-left corner to the bottom-right
    corner. Keep in mind that only right and down movements are
    allowed. 0 represents an empty space while 1 represents a wall.

    >>> matrix = [
    ...     [0, 0, 1],
    ...     [0, 0, 1],
    ...     [1, 0, 0]
    ... ]
    >>> number_of_paths(matrix)
    2
    """
    assert matrix and matrix[0], 'MATRIX must be a 2D list.'
    assert not matrix[0][0] and not matrix [-1][-1], 'MATRIX must have valid starting and ending points.'

    return number_of_paths_backtrack(matrix, (0, 0), (len(matrix)-1, len(matrix[0])-1), 0)

def number_of_paths_backtrack(matrix, start, end, res):
    if start == end:
        res += 1
    else:
        r, c = start
        for x, y in (r, c+1), (r+1, c):
            if is_valid(matrix, x, y):
                res = number_of_paths_backtrack(matrix, (x, y), end, res)
    return res

def is_valid(matrix, x, y):
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] == 0