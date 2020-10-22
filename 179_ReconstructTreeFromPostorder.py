import bisect

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        self.print_nodes(self)
        return ''

    def print_nodes(self, node, indent=0):
        if node:
            whitespace = '    ' * indent
            print(whitespace + str(node.val))

            self.print_nodes(node.left, indent + 1)
            self.print_nodes(node.right, indent + 1)

class BST:
    def __init__(self):
        self.root = None

    def __repr__(self):
        return repr(self.root)

    def postorder(self):
        nodes = []
        def postorder_recur(root):
            if root:
                postorder_recur(root.left)
                postorder_recur(root.right)
                nodes.append(root.val)
        postorder_recur(self.root)
        return nodes

def reconstruct(keys):
    """Given a sequence of KEYS visited by a postorder traversal of a
    binary search tree, reconstructs the tree.

    >>> t1 = reconstruct([2, 4, 3, 8, 7, 5])
    >>> t1
    5
        3
            2
            4
        7
            8
    <BLANKLINE>
    >>> t2 = BST()
    >>> t2.root = Node(1, None, Node(3, Node(2), None))
    >>> t2
    1
        3
            2
    <BLANKLINE>
    >>> reconstruct(t2.postorder())
    1
        3
            2
    <BLANKLINE>
    """

    if keys:
        val = keys.pop()
        root = Node(val)

        ind = bisect.bisect(keys, val)
        root.left = reconstruct(keys[:ind])
        root.right = reconstruct(keys[ind:])

        return root