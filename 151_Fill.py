def fill(matrix, loc, c):
    """Given a 2-D matrix MATRIX representing an image, a location LOC of a
    pixel on the screen, and a color C, replaces the color of the given pixel
    and all adjacent same colored pixels with C.

    >>> matrix = [['B', 'B', 'W'],
    ...           ['W', 'W', 'W'],
    ...           ['W', 'W', 'W'],
    ...           ['B', 'B', 'B']]
    >>> fill(matrix, (2, 2), 'G')
    >>> matrix
    [['B', 'B', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G'], ['B', 'B', 'B']]
    """
    assert matrix, 'Cannot fill empty matrix.'
    assert 0 <= loc[0] < len(matrix) and 0 <= loc[1] < len(matrix[0]), 'Location of pixel is not in the matrix.'
    assert isinstance(c, str) and len(c) == 1, 'C must be a character.'

    row, col = loc
    fill.starting_color = matrix[row][col]

    def bfs(matrix, loc, c, visited):
        if is_valid(matrix, loc, visited):
            visited.add(loc)
            x, y = loc
            matrix[x][y] = c
            for row, col in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
                bfs(matrix, (row, col), c, visited)
            
    def is_valid(matrix, loc, visited):
        x, y = loc
        if x < 0 or x >= len(matrix):
            return False
        elif y < 0 or y >= len(matrix[0]):
            return False
        elif matrix[x][y] != fill.starting_color:
            return False

        if loc in visited:
            return False

        return True

    bfs(matrix, loc, c, set())