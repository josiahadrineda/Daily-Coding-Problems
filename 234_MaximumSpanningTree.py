def max_spanning_tree(g):
    """Given a weighted, undirected, connected graph G, computes the maximum spanning tree of G.

    >>> max_spanning_tree({'a': [('b', 1), ('c', 2)], 'b': [('a', 1), ('c', 3)], 'c': [('a', 2), ('b', 3)]})
    {'a': [('c', 2)], 'b': [('c', 3)], 'c': [('a', 2), ('b', 3)]}
    """
    assert g, 'G cannot be an empty dictionary.'

    def has_cycle(g):
        def has_cycle_recur(curr, visited):
            if curr in visited:
                return True

            visited.add(curr)
            for neighbor, weight in g[curr]:
                if has_cycle_recur(neighbor, visited):
                    return True
            return False

    def add_node(g, x):
        src, dest, weight = x
        if not g.get(src):
            g[src] = []
        g[src].append((dest, weight))
        if not g.get(dest):
            g[dest] = []
        g[dest].append((src, weight))

    edges = []
    for k,v in g.items():
        src = k
        for dest, weight in v:
            if (dest, src, weight) not in edges:
                edges.append((src, dest, weight))
    edges.sort(key=lambda x: -x[2])

    res = {}
    i, e, n = 0, 0, len(g.keys())
    while e < n - 1:
        x = edges[i]
        if not has_cycle(res):
            add_node(res, x)
            e += 1
        i += 1
    return {k: sorted(res[k]) for k in sorted(res)}