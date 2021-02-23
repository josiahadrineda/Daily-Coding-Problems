AXIS_DIRS = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]

DIAG_DIRS = [
    (1, 1),
    (-1, 1),
    (1, -1),
    (-1, -1)
]

DIAG_FUNCS = {
    (1, 1): lambda matrix, i, j: matrix[i-1][j] != 'fs' and matrix[i][j-1] != 'fs',
    (-1, 1): lambda matrix, i, j: matrix[i+1][j] != 'bs' and matrix[i][j-1] != 'bs',
    (1, -1): lambda matrix, i, j: matrix[i-1][j] != 'bs' and matrix[i][j+1] != 'bs',
    (-1, -1): lambda matrix, i, j: matrix[i+1][j] != 'fs' and matrix[i][j+1] != 'fs'
}

def regions(matrix):
    """Given a 2D matrix, where each cell is either 'fs' (forward slash),
    'bs' (backslash), or '', returns the number of regions the slashes divide the space.

    >>> matrix = [
    ...     ['bs', '', '', '', '', 'fs'],
    ...     ['', 'bs', '', '', 'fs', ''],
    ...     ['', '', 'bs', 'fs', '', '']
    ... ]
    >>> regions(matrix)
    3
    """
    assert matrix, 'MATRIX cannot be an empty list.'

    def is_valid(i, j):
        if i < 0 or i >= m or j < 0 or j >= n:
            return False
        if matrix[i][j] != '':
            return False
        return True

    def get_dirs(i, j):
        dirs = []
        for dir_i, dir_j in AXIS_DIRS:
            ni, nj = i + dir_i, j + dir_j
            if is_valid(ni, nj):
                dirs.append((ni, nj))
        for dir_i, dir_j in DIAG_DIRS:
            ni, nj = i + dir_i, j + dir_j
            if is_valid(ni, nj) and DIAG_FUNCS[(dir_i, dir_j)](matrix, ni, nj):
                dirs.append((ni, nj))
        return dirs

    def bfs(i, j, id):
        q = [(i, j)]
        while q:
            r, c = q.pop(0)
            matrix[r][c] = id
            for nr, nc in get_dirs(r, c):
                q.append((nr, nc))

    m, n = len(matrix), len(matrix[0])

    reg = 0
    for r in range(m):
        for c in range(n):
            cell = matrix[r][c]
            if cell == '':
                bfs(r, c, reg)
                reg += 1
    return reg
