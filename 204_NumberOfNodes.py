class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root = None

def number_of_nodes(root):
    """Given the root of a complete binary tree ROOT, returns the number
    of nodes in faster than O(n) time.

    >>> t =  Tree()
    >>> t.root = Node(1, Node(2, Node(4, Node(8), Node(9)), Node(5)), Node(3, Node(6), Node(7)))
    >>> number_of_nodes(t.root)
    9
    """
    
    if not root:
        return 0
    
    l_dep, r_dep = get_dep(root.left), get_dep(root.right)
    if l_dep == r_dep:
        return (1 << l_dep) + number_of_nodes(root.right)
    return (1 << r_dep) + number_of_nodes(root.left)

def get_dep(root):
    if not root:
        return 0
    return 1 + get_dep(root.left)