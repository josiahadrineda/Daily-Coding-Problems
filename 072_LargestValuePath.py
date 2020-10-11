from collections import defaultdict

def largest_value_path(str, graph):
    graph_dict = {}
    nodes = set()
    for s,e in graph:
        if not graph_dict.get((s, str[e])):
            graph_dict[(s, str[e])] = []
        graph_dict[(s, str[e])].append((e, str[e]))
        nodes.add(s)
        nodes.add(e)

    for ind,c in graph_dict.keys():
        max_val = find_largest_value_path(graph_dict, (ind,c), [(ind,c)], 1)
    return max_val

def find_largest_value_path(graph_dict, node, path, max_val):
    if not graph_dict.get(node):
        pass
    else:
        for neighbor in graph_dict[node]:
            if neighbor in path:
                return None
            path.append(neighbor)
            find_largest_value_path(graph_dict, neighbor, path, max_val)
            path.pop()
    max_val += evaluate_largest_value_path(path) + 1
    return max_val

def evaluate_largest_value_path(path):
    nodes = defaultdict(int)
    for ind,c in path:
        nodes[c] += 1
    return max(nodes.values())

assert largest_value_path("ABACA", [(0,1),(0,2),(2,3),(3,4)]) == 3
assert largest_value_path("A", [(0,0)]) == None