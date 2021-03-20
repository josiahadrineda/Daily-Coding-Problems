class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class CartesianTree:
    def __init__(self, seq):
        self.seq = seq
        self.root = self.construct_cartesian_tree(list(self.seq))

    # O(N^2) intuitive algorithm. There is an O(N*log N) solution, but I don't know it.
    def construct_cartesian_tree(self, seq):
        if not seq:
            return None

        min_idx = seq.index(min(seq))
        node = Node(seq[min_idx])

        node.left = self.construct_cartesian_tree(seq[:min_idx])
        node.right = self.construct_cartesian_tree(seq[min_idx + 1:])
        
        return node

def is_cartesian_tree(ct):
    """Determines whether a given tree CT is a Cartesian Tree (min heap variation).

    >>> ct = CartesianTree([3, 2, 6, 1, 9])
    >>> is_cartesian_tree(ct)
    True
    >>> ct2 = CartesianTree([5, 10, 40, 30, 28])
    >>> is_cartesian_tree(ct2)
    True
    """

    def inorder(root):
        if not root:
            return []
        seq = inorder(root.left) + [root.val] + inorder(root.right)
        return seq

    def is_min_heap(root):
        if not root:
            return True
        
        if root.left and root.val >= root.left.val:
            return False
        if root.right and root.val >= root.right.val:
            return False
        return is_min_heap(root.left) and is_min_heap(root.right)

    return inorder(ct.root) == ct.seq and is_min_heap(ct.root)