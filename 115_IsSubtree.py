class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Val: {self.val}'

class Tree:
    def __init__(self):
        self.root = None

    def __repr__(self):
        root = self.root
        nodes = []
        q = [root]
        while q:
            curr = q.pop(0)
            nodes.append(curr.val)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return str(nodes)

def is_subtree(s, t):
    """
    Given two non-empty binary trees s and t,
    checks whether tree t has exactly the same
    structure and node values with a subtree of s.


    >>> s = Tree()
    >>> s.root = Node(3, Node(2), Node(1))
    >>> t = Tree()
    >>> t.root = Node(7, Node(6, Node(5), Node(4)), Node(3, Node(2), Node(1)))
    >>> is_subtree(s, t)
    True
    >>> is_subtree(t, s)
    False
    >>> t.root = Node(3, Node(2), Node(1, Node(0)))
    >>> is_subtree(s, t)
    False
    """

    s_root, t_root = s.root, t.root
    q = [t_root]
    while q:
        curr = q.pop(0)
        if is_eq(s_root, curr):
            return True
        else:
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
    return False

def is_eq(s_root, t_root):
    """
    Given the roots of two trees s and t,
    determines whether they are equal in
    terms of structure and node values.
    """

    if not s_root and not t_root:
        return True
    elif (s_root and not t_root) or (not s_root and t_root):
        return False
    elif s_root.val != t_root.val:
        return False
    return is_eq(s_root.left, t_root.left) and is_eq(s_root.right, t_root.right)