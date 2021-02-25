DIRS = [
    (-2, 1),
    (-1, 2),
    (1, 2),
    (2, 1),
    (2, -1),
    (1, -2),
    (-1, -2),
    (-2, -1)
]

def prob(coord, k):
    """A knight is placed on a given square on an 8x8 chess board. It isi then moved
    randomly several times, where each move is a standard knight move. If the knight
    jumps off the board at any point, it is not allowed to jump back on.

    Given an (x, y) coordinate COORD and positive integer K, computes the probability
    that a knight remains on the board after K moves.

    >>> prob((4, 4), 1)
    1.0
    >>> prob((1, 1), 3)
    0.11
    """
    assert 1 <= coord[0] <= 8, 'X coordinate in COORD must be in the range of 1 - 8.'
    assert 1 <= coord[1] <= 8, 'Y coordinate in COORD must be in the range of 1 - 8.'
    assert k > 0, 'K must be a positive integer.'

    def is_valid(x, y):
        return 1 <= x <= 8 and 1 <= y <= 8

    def bfs(coord, k):
        q = [((coord), 0)]
        res = 0
        while q:
            curr_coord, curr_move = q.pop(0)
            x, y = curr_coord
            if curr_move == k:
                res += 1
                continue
            for dir_x, dir_y in DIRS:
                nx, ny = x + dir_x, y + dir_y
                if is_valid(nx, ny):
                    q.append(((nx, ny), curr_move + 1))
        return res

    numer = bfs(coord, k)
    denom = sum([8**exp for exp in range(1, k + 1)])
    return round(numer / denom, 2)