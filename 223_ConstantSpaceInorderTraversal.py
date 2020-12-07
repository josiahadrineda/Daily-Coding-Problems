class Tree:
    def __init__(self):
        self.root = None

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder(root):
    """Given the root of a binary tree ROOT, computes its inorder traversal
    in O(1) space.

    >>> t = Tree()
    >>> t.root = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
    >>> inorder(t.root)
    [1, 2, 3, 4, 5, 6, 7]
    """

    # NODES list does not count as extra space.
    nodes = []
    curr = root
    while curr:
        if not curr.left:
            nodes.append(curr.val)
            curr = curr.right
        else:
            prev = curr.left
            while prev.right and prev != curr:
                prev = prev.right

            if not prev.right:
                prev.right = curr
                curr = curr.left
            else:
                nodes.append(curr.val)
                curr = curr.right
    return nodes