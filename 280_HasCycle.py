def has_cycle(graph):
    """Given an undirected graph (in dictionary adjacency list form) GRAPH, determines
    whether or not GRAPH contains a cycle. The nodes of GRAPH will be labeled from
    0 ... N.

    **Note: GRAPH will always be valid.**

    >>> graph = {
    ...     0: [1, 2],
    ...     1: [3, 4],
    ...     2: [5, 6]
    ... }
    >>> has_cycle(graph)
    False
    >>> has_cycle({0: [1, 2], 1: [2]})
    True
    >>> has_cycle({0: [0]})
    True
    """
    assert graph, 'GRAPH cannot be an empty dictionary.'

    def dfs(node):
        if node in visited:
            return True
        else:
            visited.add(node)
            if graph.get(node) == None:
                return False
            else:
                for neighbor in graph[node]:
                    if dfs(neighbor):
                        return True
                return False

    visited = set()
    return dfs(0)