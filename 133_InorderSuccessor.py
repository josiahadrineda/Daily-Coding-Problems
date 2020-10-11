class Node:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return str(self.val)

def inorder_successor(root, node):
    """Given the root of a binary search tree and a node value, returns
    the next biggest element, aka inorder successor, if there is one.

    >>> root = Node(10, Node(5), Node(30, Node(22), Node(35)))
    >>> root.left.parent = root
    >>> root.right.parent = root
    >>> root.right.left.parent = root.right
    >>> root.right.right.parent = root.right
    >>> inorder_successor(root, 22)
    30
    >>> inorder_successor(root, 30)
    35
    >>> inorder_successor(root, 35)
    -1
    """
    assert root, 'Cannot find inorder successor of empty binary search tree.'

    r = binary_search(root, node)
    return find_successor(r)

def binary_search(root, node):
    while root.val != node:
        if root.val < node:
            root = root.right
        else:
            root = root.left
    return root

def find_successor(root):
    if root.parent and root.right:
        if root.right.val > root.val:
            return root.right.val
        elif root.parent.val > root.val:
            return root.parent.val
    elif root.parent:
        return root.parent.val if root.parent.val > root.val else -1
    elif root.right:
        return root.right.val if root.right.val > root.val else -1
    return -1