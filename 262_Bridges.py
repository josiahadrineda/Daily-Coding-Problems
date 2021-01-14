def bridges(graph):
    """Given a graph GRAPH, locates all the bridges in GRAPH, where a bridge is an edge
    that disconnects GRAPH if removed.

    **Note: GRAPH should be a connected, undirected graph.**

    >>> bridges({0: [1, 2, 3], 1: [0, 2], 2: [0, 1], 3: [0, 4], 4: [3]}) == set([(0, 3), (3, 4)])
    True
    >>> bridges({0: [1], 1: [0, 2], 2: [1, 3], 3: [2]}) == set([(0, 1), (1, 2), (2, 3)])
    True
    >>> bridges({0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}) == set([])
    True
    """
    assert graph, 'GRAPH cannot be an empty graph.'

    def is_connected(graph, num_nodes):
        def connected_recur(node, visited):
            visited.add(node)
            res = 1
            for neighbor in graph[node]:
                if neighbor not in visited:
                    res += connected_recur(neighbor, visited)
            return res

        return connected_recur(0, set()) == num_nodes

    num_nodes = len(graph.keys())
    visited = set()
    res = set()
    for k in graph.keys():
        for v in list(graph[k]):
            if (v, k) not in visited:
                visited.add((k, v))

                graph[k].remove(v)
                graph[v].remove(k)
                if not is_connected(graph, num_nodes):
                    res.add((k, v))
                graph[k].append(v)
                graph[v].append(k)
    
    return res