def valid_crossword_grid(grid):
    """Given an N by N grid of black and white squares ('b' or 'w') GRID, determines
    whether GRID is a valid crossword grid using the following rules:

    1. Every white square must be part of an "across" word and a "down" word
    2. No word can be fewer than three letters long
    3. Every white square must be reachable from every other white square

    **Note: A typical American-style crossword grid is rotationally symmetric, but I
    am not testing for that rule here for the sake of simplicity.**

    >>> grid = [
    ...     ['b', 'w', 'b', 'b'],
    ...     ['b', 'w', 'b', 'b'],
    ...     ['b', 'w', 'b', 'b'],
    ...     ['b', 'w', 'b', 'b']    
    ... ]
    >>> valid_crossword_grid(grid)
    False
    >>> grid = [
    ...     ['b', 'w', 'b', 'w'],
    ...     ['b', 'w', 'b', 'w'],
    ...     ['b', 'w', 'b', 'w'],
    ...     ['b', 'w', 'b', 'w']    
    ... ]
    >>> valid_crossword_grid(grid)
    False
    >>> grid = [
    ...     ['b', 'w', 'w', 'b'],
    ...     ['b', 'w', 'b', 'b'],
    ...     ['w', 'w', 'w', 'w'],
    ...     ['b', 'w', 'b', 'b']    
    ... ]
    >>> valid_crossword_grid(grid)
    False
    >>> grid = [
    ...     ['b', 'w', 'w', 'w'],
    ...     ['b', 'w', 'b', 'b'],
    ...     ['w', 'w', 'w', 'w'],
    ...     ['b', 'w', 'b', 'b']    
    ... ]
    >>> valid_crossword_grid(grid)
    True
    """
    assert grid, 'GRID cannot be an empty list.'
    assert len(grid) == len(grid[0]), 'GRID must be N by N.'

    n = len(grid)

    min_word_len, valid_word_cnt, white_cnt = float('inf'), 0, 0
    s, first = None, True   # For use in reachability scan below

    # Scan for "across" words
    for r in range(n):
        prev, streak = None, 0
        for c in range(n):
            square = grid[r][c]
            if square == 'w':
                white_cnt += 1
                if first:
                    s = (r, c)
                    first = False
                if prev == square:
                    streak += 1
            prev = square

        if streak:
            streak += 1
            min_word_len = min(min_word_len, streak)
            if streak >= 3:
                valid_word_cnt += 1

    # Scan for "down" words
    for c in range(n):
        prev, streak = None, 0
        for r in range(n):
            square = grid[r][c]
            if 'w' == prev == square:
                streak += 1
            prev = square

        if streak:
            streak += 1
            min_word_len = min(min_word_len, streak)
            if streak >= 3:
                valid_word_cnt += 1

    if min_word_len < 3:
        return False
    if valid_word_cnt <= 1:
        return False

    # Scan for white square reachability
    q, visited, cnt = [s], set(), 0
    while q:
        curr = q.pop(0)
        visited.add(curr)
        cnt += 1

        r, c = curr
        for dir_r, dir_c in (1, 0), (-1, 0), (0, 1), (0, -1):
            nr, nc = dir_r + r, dir_c + c
            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited and grid[nr][nc] == 'w':
                q.append((nr, nc))    
    if cnt != white_cnt:
        return False

    return True