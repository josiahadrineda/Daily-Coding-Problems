class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        s = f'Node({self.val}'
        if self.left: s += f', {repr(self.left)}'
        if self.right: s += f', {repr(self.right)}'
        s += ')'
        return s

class Tree:
    def __init__(self):
        self.root = None

    def __repr__(self):
        return repr(self.root)

def merge(root1, root2):
    """Given the roots of two binary trees ROOT1 and ROOT2, merges the two roots into one, where each node
    in the new root holds a value equal to the sum of the values of the corresponding nodes of the inputs.

    >>> t1 = Tree()
    >>> t1.root = Node(1, Node(1, Node(4), Node(5)), Node(1))
    >>> t2 = Tree()
    >>> t2.root = Node(0, Node(1), Node(2, Node(6), Node(7)))
    >>> t_merge = Tree()
    >>> t_merge.root = merge(t1.root, t2.root)
    >>> t_merge
    Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
    """
    
    # This version might retain some of the input roots, hence modifying the input roots afterwards might
    # lead to modification of the merged output. To circumvent this, must make copies of the input roots.
    def merge_recur(r1, r2):
        if not r1:
            return r2
        elif not r2:
            return r1
        return Node(
            r1.val + r2.val,
            merge_recur(r1.left, r2.left),
            merge_recur(r1.right, r2.right)
        )
    return merge_recur(root1, root2)