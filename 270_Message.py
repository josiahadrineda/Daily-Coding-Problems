def message_time(edges):
    """Given a list of edges 0...N EDGES in the format [(start, end, time)], where 'time'
    is the time it takes for a message to be passed from 'start' to 'end', determines
    how long it will take for every node to receive a message that begins at node 0.

    **Note: Assume that the graph formed by EDGES is connected.**

    >>> edges = [
    ...     (0, 1, 5), 
    ...     (0, 2, 3),
    ...     (0, 5, 4),
    ...     (1, 3, 8),
    ...     (2, 3, 1), 
    ...     (3, 5, 10), 
    ...     (3, 4, 5)
    ... ]
    >>> message_time(edges)
    9
    >>> message_time([(0, 1, 5), (0, 2, 4), (0, 3, 3)])
    5
    >>> message_time([(0, 0, 0)])
    0
    """
    assert edges, 'EDGES cannot be an empty list.'

    graph, times, curr_times, n = {}, {}, {}, 0
    for (s, e, t) in edges:
        if graph.get(s) == None:
            graph[s] = []
        graph[s].append(e)
        if graph.get(e) == None:
            graph[e] = []
        graph[e].append(s)

        times[(s, e)] = t
        times[(e, s)] = t

        curr_times[(s, e)] = 0
        curr_times[(e, s)] = 0

        n = max(n, s, e)
    n += 1

    def bfs(visited, curr_times):
        q = []
        for neighbor in graph[0]:
            q.append((0, neighbor, 0))

        time = 0
        while True:
            for (s, e, curr_time) in list(q):
                q.pop(0)
                if curr_time == times[(s, e)]:
                    visited[e] = True
                    if all(visited):
                        return time
                    for neighbor in graph[e]:
                        q.append((e, neighbor, 1))
                else:
                    q.append((s, e, curr_time + 1))
            time += 1

    visited = [False] * n
    visited[0] = True
    return bfs(visited, curr_times) if n > 1 else 0