class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def search(self, x):
        if x == self.val:
            return True
        elif x < self.val:
            return self.left.search(x) if self.left else False
        return self.right.search(x) if self.right else False

class Tree:
    def __init__(self):
        self.root = None

    def search(self, x):
        return self.root.search(x)

    def bounds(self, x):
        """Given a BST (this doesn't check the validity of the BST btw) and an
        integer X, determines the bounds of X.

        >>> t = Tree()
        >>> t.root = Node(8, Node(4, Node(2), Node(6)), Node(12, Node(10), Node(14)))
        >>> t.bounds(7)
        [6, 8]
        >>> t.bounds(10)
        [10, 10]
        >>> t.bounds(1)
        [None, 2]
        >>> t.bounds(15)
        [14, None]
        """
        assert x, 'X must be an integer.'

        root = self.root

        def lower_bound(x, node=root):
            if not node:
                return float('inf')
            elif node.val > x:
                return lower_bound(x, node.left)
            else:
                lb = lower_bound(x, node.right)
                return lb if lb < x else node.val

        def upper_bound(x, node=root):
            if not node:
                return float('-inf')
            elif node.val < x:
                return upper_bound(x, node.right)
            else:
                ub = upper_bound(x, node.left)
                return ub if ub > x else node.val

        if self.search(x):
            return [x, x]

        lb = lower_bound(x)
        if lb == float('inf'):
            lb = None
        ub = upper_bound(x)
        if ub == float('-inf'):
            ub = None
        return [lb, ub]