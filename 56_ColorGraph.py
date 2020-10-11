from collections import defaultdict

def color_graph(matrix, k):
    n = len(matrix)
    if not matrix or n == 0:
        return False
    if k < 1:
        return False
    elif k == 1 and n > 1:
        return False
    elif k >= n:
        return True

    graph = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                graph[j].append(i)

    nodes = [-1 for _ in range(n)]
    return color(graph, nodes, 0, k)

def color(graph, nodes, ind, k):
    if ind == len(nodes):
        return True
    else:
        for i in range(k):
            if is_valid(graph, nodes, ind, i):
                nodes[ind] = i
                if color(graph, nodes, ind+1, k):
                    return True
                nodes[ind] = -1
        return False

def is_valid(graph, nodes, ind, color):
    for neighbor in graph[ind]:
        if nodes[neighbor] == color:
            return False
    return True

matrix = [[0,1,1,1],
          [1,0,1,1],
          [1,1,0,1],
          [1,1,1,0]]

assert color_graph(matrix, 4)
assert not color_graph(matrix, 3)
assert not color_graph(matrix, 2)
assert not color_graph(matrix, 1)