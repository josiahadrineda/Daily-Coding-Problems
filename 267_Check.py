DIRS = {
    'P': [(-1, -1), (-1, 1)],
    'N': [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)],
    'B': [(-1, -1), (-1, 1), (1, 1), (1, -1)],
    'R': [(-1, 0), (0, 1), (1, 0), (0, -1)],
    'Q': [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
}

def check(board):
    """Given an NxN matrix representing a chess board BOARD, as well as chess pieces in
    BOARD (black king BK, and several white pieces WQ, WB, WN, WR, WP), determines
    whether BK is in check.

    **Note: Assume there is only ONE BK on BOARD.**

    >>> board = [
    ...     ['', '', '', '', '', '', '', ''],
    ...     ['WP', '', '', '', '', '', 'WN', ''],
    ...     ['', '', '', 'BK', '', '', '', ''],
    ...     ['', '', '', '', '', '', '', ''],
    ...     ['', '', '', 'WB', '', '', '', ''],
    ...     ['', '', '', '', '', '', '', ''],
    ...     ['', '', '', '', '', '', '', 'WQ'],
    ...     ['', '', 'WR', '', '', '', '', '']
    ... ]
    >>> check(board)
    True
    >>> board = [
    ...     ['BK', '', ''],
    ...     ['', '', 'WN']
    ... ]
    >>> check(board)
    True
    >>> board = [
    ...     ['', 'BK'],
    ...     ['WP', '']
    ... ]
    >>> check(board)
    True
    >>> board = [['BK', 'WR']]
    >>> check(board)
    True
    >>> board = [
    ...     ['BK', '', ''],
    ...     ['', '', ''],
    ...     ['', '', 'WB']
    ... ]
    >>> check(board)
    True
    """
    assert board, 'BOARD cannot be an empty matrix.'

    def line_of_sight(s, e, dirs, is_continuous, board):
        def is_valid(r, c, board, is_continuous, visited=None):
            if is_continuous:
                return 0 <= r < len(board) and 0 <= c < len(board[0]) and \
                    ((board[r][c] == '' or board[r][c] == 'BK') and (r, c) not in visited)
            return 0 <= r < len(board) and 0 <= c < len(board[0]) and \
                (board[r][c] == '' or board[r][c] == 'BK')

        def sight_static(s, e, poss, board):
            r, c = s
            for pos in poss:
                pos_r, pos_c = pos
                temp_r, temp_c = pos_r + r, pos_c + c
                if is_valid(temp_r, temp_c, board, False):
                    if (temp_r, temp_c) == e:
                        return True
            return False

        def sight_continuous(s, e, dirs, board, visited):
            if s == e:
                return True
            else:
                visited.add(s)
                r, c = s
                for dir in dirs:
                    dir_r, dir_c = dir
                    temp_r, temp_c = dir_r + r, dir_c + c
                    if is_valid(temp_r, temp_c, board, True, visited):
                        if sight_continuous((temp_r, temp_c), e, dirs, board, visited):
                            return True
                return False

        if is_continuous:
            return sight_continuous(s, e, dirs, board, set())
        return sight_static(s, e, dirs, board)

    e = None
    ps, ns, bs, rs, qs = [], [], [], [], []
    for i in range(len(board)):
        for j in range(len(board[0])):
            pos, cell = (i, j), board[i][j]
            if cell == 'BK':
                e = pos
            elif cell == 'WP':
                ps.append(pos)
            elif cell == 'WN':
                ns.append(pos)
            elif cell == 'WB':
                bs.append(pos)
            elif cell == 'WR':
                rs.append(pos)
            elif cell == 'WQ':
                qs.append(pos)
                
    # Checks
    for s in ps:
        if line_of_sight(s, e, DIRS['P'], False, board):
            return True

    for s in ns:
        if line_of_sight(s, e, DIRS['N'], False, board):
            return True

    for s in bs:
        if line_of_sight(s, e, DIRS['B'], True, board):
            return True

    for s in rs:
        if line_of_sight(s, e, DIRS['R'], True, board):
            return True

    for s in qs:
        if line_of_sight(s, e, DIRS['Q'], True, board):
            return True

    return False