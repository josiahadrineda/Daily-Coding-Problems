def max_words(bo, d):
    """Given a matrix of lowercase letters BO and a dictionary of lowercase words D,
    finds the maximum number of words that can fit on BO (found by stringing together
    characters that are adjacent vertically and horizontally) without them overlapping.

    >>> bo = [
    ...     ['e', 'a', 'n'],
    ...     ['t', 't', 'i'],
    ...     ['a', 'r', 'a']
    ... ]
    >>> max_words(bo, ['eat', 'rain', 'in', 'rat'])
    3
    >>> max_words(bo, ['at', 'eat', 'rain', 'train'])
    3
    """
    assert bo, 'BO cannot be an emtpy matrix.'
    assert d, 'D cannot be an empty list.'

    def max_words_recur(d):
        res = 0
        for i,w in enumerate(d):
            for _ in configurations(w):
                res = max(res, 1 + max_words_recur(d[:i] + d[i + 1:]))
                if res == len(d): return res
        return res

    def configurations(w):
        def dfs(r, c, w):
            if not w:
                yield True
            elif not is_valid(r, c, w):
                yield False
            else:
                visited[r][c] = True
                for dir_r, dir_c in (0, 1), (1, 0), (0, -1), (-1, 0):
                    nr, nc = r + dir_r, c + dir_c
                    yield from dfs(nr, nc, w[1:])
                visited[r][c] = False

        def is_valid(r, c, w):
            return 0 <= r < m and 0 <= c < n \
                and visited[r][c] == False \
                and bo[r][c] == w[0]

        for r in range(m):
            for c in range(n):
                for valid_conf in dfs(r, c, w):
                    if valid_conf:
                        yield

    def mark(visited, trace, marker):
        for r,c in trace:
            visited[r][c] = marker

    m, n = len(bo), len(bo[0])
    visited = [[False] * n for _ in range(m)]
    return max_words_recur(d)