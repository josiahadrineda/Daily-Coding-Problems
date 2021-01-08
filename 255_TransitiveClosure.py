def transitive_closure(adj):
    """Given a graph in adjacency list form ADJ, computes
    ADJ's transitive closure, where "transitive closure" is
    defined as an N x N matrix (N = # nodes) M, where M[i][j]
    is 1 if there exists a path between i and j and 0 otherwise.

    >>> adj = [
    ...     [0, 1, 3],
    ...     [1, 2],
    ...     [2],
    ...     [3]
    ... ]
    >>> transitive_closure(adj)
    [[1, 1, 1, 1], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    """
    assert adj, 'ADJ cannot be an empty matrix.'

    def a_to_b(a, b):
        if a == b:
            return True
        return any([a_to_b(c, b) for c in adj[a][1:]])

    n = len(adj)
    res = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if a_to_b(i, j):
                res[i][j] = 1
    return res