class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        l, r = repr(self.left), repr(self.right)
        if l == 'None': l = ''
        if r == 'None': r = ''
        
        if not l and not r:
            return f'Node({self.val})'
        elif l and not r:
            return f'Node({self.val}, {l})'
        elif not l and r:
            return f'Node({self.val}, {r})'
        else:
            return f'Node({self.val}, {l}, {r})'

class Tree:
    def __init__(self):
        self.root = None

    def __repr__(self):
        return repr(self.root)

def convert_to_full_binary_tree(t):
    """Given a binary tree T, converts T into a full binary tree.

    **Note: A full binary tree is a tree whose nodes have either both
    the left and right children or no children.**

    >>> t = Tree()

    >>> t.root = Node(0, Node(1, Node(3, None, Node(5))), Node(2, None, Node(4, Node(6), Node(7))))
    >>> convert_to_full_binary_tree(t)
    >>> t.root
    Node(0, Node(5), Node(4, Node(6), Node(7)))

    >>> t.root = Node(0, Node(1, Node(2, Node(3, Node(4)))))
    >>> convert_to_full_binary_tree(t)
    >>> t.root
    Node(4)

    >>> t.root = Node(0)
    >>> convert_to_full_binary_tree(t)
    >>> t.root
    Node(0)
    """
    assert t.root, 'T cannot be an empty binary tree.'

    def convert_recur(root):
        if not root or (not root.left and not root.right):
            pass
        elif root.left and not root.right:
            root = convert_recur(root.left)
        elif not root.left and root.right:
            root = convert_recur(root.right)
        else:
            root.left = convert_recur(root.left)
            root.right = convert_recur(root.right)
        return root

    t.root = convert_recur(t.root)