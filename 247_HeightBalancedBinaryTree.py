class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def is_leaf(self):
        return not self.left and not self.right

class Tree:
    def __init__(self):
        self.root = None

    def is_height_balanced(self):
        """A binary tree is height balanced if the heights
        of both subtrees of any node never differ by more
        than one. Determines whether a Tree satisfies
        this property.

        >>> t = Tree()
        >>> t.root = Node(1, Node(2, Node(4)), Node(3, Node(5), Node(6)))
        >>> t.is_height_balanced()
        True
        >>> t.root = Node(1, Node(2, Node(3)))
        >>> t.is_height_balanced()
        False
        """

        def balanced_recur(root):
            if root.is_leaf():
                return True
            else:
                l, r = 0, 0
                if root.left:
                    if not balanced_recur(root.left):
                        return False
                    l = height(root.left)
                if root.right:
                    if not balanced_recur(root.right):
                        return False
                    r = height(root.right)
                return abs(l - r) <= 1

        def height(root):
            if root.is_leaf():
                return 1
            else:
                l, r = 0, 0
                if root.left:
                    l = height(root.left)
                if root.right:
                    r = height(root.right)
                return 1 + max(l, r)

        return balanced_recur(self.root)