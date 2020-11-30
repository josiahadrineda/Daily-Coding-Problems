class Tree:
    def __init__(self):
        self.root = None

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bottom_view(root):
    """Given the root to a binary tree ROOT, returns one possible bottom view, where
    bottom view is defined as the nodes that are seen looking at the binary tree
    from the bottom up.

    **Note: If two nodes occupy the same space, either node can be selected.**

    >>> t = Tree()
    >>> t.root = Node(2, Node(1), Node(3, Node(4), Node(5)))
    >>> bottom_view(t.root)
    [1, 4, 3, 5]
    >>> t2 = Tree()
    >>> t2.root = Node(5, Node(3, Node(1, Node(0)), Node(4)), Node(7, Node(6), Node(9, Node(8))))
    >>> bottom_view(t2.root)
    [0, 1, 3, 6, 8, 9]
    """
    assert root, 'ROOT cannot be an empty binary tree.'

    view = {}
    q = [(root, 0)]
    while q:
        curr, dist = q.pop(0)
        view[dist] = curr.val
        if curr.left:
            q.append((curr.left, dist - 1))
        if curr.right:
            q.append((curr.right, dist + 1))
    return [v for k,v in sorted(view.items())]