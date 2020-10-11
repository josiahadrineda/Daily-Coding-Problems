from collections import defaultdict

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)

class Tree:
    def __init__(self):
        self.root = None

    def __repr__(self):
        if not self.root:
            return
        return f'Tree({self.root.val}, left=Tree({repr(self.root.left)}), right=Tree({repr(self.root.right)}))'

def minimum_sum(t):
    """
    Given a binary tree, returns the level of the tree with minimum sum

    >>> t = Tree()
    >>> t.root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
    >>> minimum_sum(t)
    1
    """
    assert t, 'Cannot determine the sum of an empty binary tree.'

    level_sums = defaultdict(int)
    q = [(t.root, 1)]
    while q:
        curr, level = q.pop(0)
        level_sums[level] += curr.val
        if curr.left:
            q.append((curr.left, level + 1))
        if curr.right:
            q.append((curr.right, level + 1))

    res, min_sum = 0, float('inf')
    for k,v in level_sums.items():
        if v < min_sum:
            res, min_sum = k, v
    return res