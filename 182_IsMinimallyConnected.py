# https://cs.stackexchange.com/questions/52157/determining-if-an-undirected-connected-graph-is-minimally-connected
# https://www.geeksforgeeks.org/count-number-edges-undirected-graph/

def is_minimally_connected(graph):
    """Given an undirected graph GRAPH, ckecks if GRAPH is minimally connected.

    *Minimally connected = GRAPH is connected and there is no edge that can
    be removed while still leaving the graph connected*

    >>> adj_list = [[1, 2], [0], [0]]
    >>> is_minimally_connected(adj_list)
    True
    >>> adj_list = [[1, 2], [0, 2], [0, 1]]
    >>> is_minimally_connected(adj_list)
    False
    """
    assert isinstance(graph, list), 'GRAPH must be an adjacency LIST.'

    vertices = len(graph)
    edges = sum([len(k) for k in graph]) // 2
    
    return vertices == edges + 1