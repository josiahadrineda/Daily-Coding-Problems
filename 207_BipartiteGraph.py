def bipartite_graph(g):
    """Given an undirected graph G, checks whether G is bipartite. Recall
    that a graph is bipartite if its vertices can be divided into two
    independent sets, U and V, such that no edge connects vertices of the
    same set.

    >>> bipartite_graph({1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [1, 3]})
    True
    >>> bipartite_graph({1: [2, 3, 4], 2: [1, 3, 4], 3: [1, 2], 4: [1, 2]})
    False
    """
    assert g, 'G cannot be an empty graph.'

    src = list(g.keys())[0]
    u, v = set([src]), set()
    q = [(src, 0)]
    while q:
        curr, color = q.pop(0)
        for neighbor in g[curr]:
            if color == 0:
                if neighbor in u:
                    return False
                if neighbor not in v:
                    v.add(neighbor)
                    q.append((neighbor, 1 - color))
            else:
                if neighbor in v:
                    return False
                if neighbor not in u:
                    u.add(neighbor)
                    q.append((neighbor, 1 - color))
    return True