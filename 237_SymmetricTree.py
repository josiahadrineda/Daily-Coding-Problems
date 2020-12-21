class Node:
    def __init__(self, label, branches=[]):
        self.label = label
        self.branches = branches

    def __eq__(self, other):
        if self.is_leaf():
            return other.is_leaf() and self.label == other.label
        elif len(self.branches) != len(other.branches):
            return False
        else:
            return self.label == other.label and \
                all([b == ob for b, ob in zip(self.branches, other.branches)])

    def is_leaf(self):
        return not self.branches

class Tree:
    def __init__(self, root=None):
        self.root = root

    def __eq__(self, other):
        return self.root == other.root

    def is_symmetric(self):
        """Determines whether a given Tree is symmetric.

        >>> t = Tree()
        >>> t.root = Node(4, [Node(3, [Node(9)]), Node(5), Node(3, [Node(9)])])
        >>> t.is_symmetric()
        True
        >>> t.root = Node(4, [Node(3, [Node(9)]), Node(5), Node(3)])
        >>> t.is_symmetric()
        False
        """

        def reverse_tree(root):
            if root.is_leaf():
                return Node(root.label)
            return Node(root.label, [reverse_tree(b) for b in root.branches[::-1]])

        root = self.root
        root_reversed = reverse_tree(root)
        tree_reversed = Tree(root_reversed)

        return tree_reversed == self