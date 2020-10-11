class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root = None

def level_order_traversal(root):
    """
    Print the node values of a binary tree by level.

    >>> t = Tree()
    >>> t.root = Node(1, Node(2), Node(3, Node(4), Node(5)))
    >>> level_order_traversal(t.root)
    '1, 2, 3, 4, 5'
    """
    assert root, 'Tree must exist.'

    nodes = []
    q = [root]
    while q:
        curr = q.pop(0)
        nodes.append(str(curr.val))
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)
    return ', '.join(nodes)