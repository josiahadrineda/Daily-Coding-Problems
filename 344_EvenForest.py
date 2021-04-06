# https://www.geeksforgeeks.org/maximum-edge-removal-tree-make-even-forest/
# If max edges -> min edges, res is bounded by [0, 1]

class Node:
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children

class Tree:
    def __init__(self):
        self.root = None

def max_edge_even_forest(t):
    """Given a Tree T, returns the maximum number of "edges" (connections between
    parent and child nodes) that can be removed while guaranteeing that all
    reesulting disconnected subtrees have an even number of nodes (even forest).

    >>> t = Tree()
    >>> t.root = Node(4, [Node(6), Node(7), Node(8)])
    >>> max_edge_even_forest(t)
    0
    >>> t.root = Node(1, [Node(2), Node(3, [t.root, Node(5)])])
    >>> max_edge_even_forest(t)
    2
    """
    assert t, 'T cannot be an empty Tree.'

    # Bottom-up, Greedy DFS
    # Guaranteed to return the maximum
    def dfs(root):
        nonlocal res

        num_nodes = 0
        for child in root.children:
            sub_nodes = dfs(child)
            if sub_nodes % 2 == 0:
                res += 1
            else:
                num_nodes += sub_nodes
        return num_nodes + 1

    res = 0
    dfs(t.root)
    return res