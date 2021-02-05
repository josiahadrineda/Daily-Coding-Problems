class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root = None

def cousins(t, n):
    """Given a binary tree T and a particular node value N, returns all cousins of N,
    where a node's cousin is defined as a node on the same level as N but having a
    different parent.

    **Note: All values in T will be unique. Also assume that N can be found within T.**

    >>> t = Tree()
    >>> t.root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6)))
    >>> sorted(cousins(t, 4))
    [6]
    >>> sorted(cousins(t, 5))
    [6]
    >>> sorted(cousins(t, 6))
    [4, 5]
    """
    assert t, 'T cannot be an empty binary tree.'
    
    def traverse(root, level, parent):
        if not root:
            return

        if levels.get(level) == None:
            levels[level] = []
        levels[level].append(root.val)
        if parents.get(root.val) == None:
            parents[root.val] = []
        parents[root.val] = parent

        traverse(root.left, level + 1, root.val)
        traverse(root.right, level + 1, root.val)

    levels, parents = {}, {}
    traverse(t.root, 0, None)

    for level in levels.values():
        if n not in level:
            continue

        n_parent = parents[n]
        cousins = []
        for node in level:
            if node != n and parents[node] != n_parent:
                cousins.append(node)
        return cousins