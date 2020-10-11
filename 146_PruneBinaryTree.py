class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        self.node_hierarchy(self, 0)
        return ''

    def node_hierarchy(self, node, indent):
        if node:
            print('    ' * indent + str(node.val))
            self.node_hierarchy(node.left, indent + 1)
            self.node_hierarchy(node.right, indent + 1)

def prune(root):
    """Given a binary tree where all nodes are either 0 or 1,
    prune the tree so that subtrees containing all 0s are removed.

    >>> t = Node(0, Node(1), Node(0, Node(1, Node(0), Node(0)), Node(0)))
    >>> t
    0
        1
        0
            1
                0
                0
            0
    <BLANKLINE>
    >>> prune(t)
    >>> t
    0
        1
        0
            1
    <BLANKLINE>
    """
    root = prune_helper(root)

def prune_helper(root):
    if not root:
        pass
    elif not root.left and not root.right:
        if root.val == 0:
            root = None
    else:
        root.left = prune_helper(root.left)
        root.right = prune_helper(root.right)
    return root