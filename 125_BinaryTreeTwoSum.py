class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def _print_all_nodes(self, index=0):
        if self:
            whitespace = '    ' * index
            print(whitespace + str(self.val))

            if self.left:
                self.left._print_all_nodes(index+1)
            if self.right:
                self.right._print_all_nodes(index+1)

class Tree:
    def __init__(self):
        self.root = None

    def __repr__(self):
        self.root._print_all_nodes()

        # Dummy string
        return ''

def tree_two_sum(root, K):
    """
    Given the root of a binary search tree and a target K,
    returns two nodes in the tree whose sum equals K.

    >>> t = Tree()
    >>> t.root = Node(10)
    >>> t.root.left = Node(5)
    >>> t.root.right = Node(15)
    >>> t.root.right.left = Node(11)
    >>> t.root.right.right = Node(15)
    >>> tree_two_sum(t.root, 20)
    (5, 15)
    """
    assert root, 'Cannot retrieve the sum of an empty tree.'

    nodes = inorder([], root)
    return bst_two_sum(nodes, K)

def inorder(nodes, root):
    if root:
        nodes = inorder(nodes, root.left)
        nodes.append(root.val)
        nodes = inorder(nodes, root.right)
    return nodes

def bst_two_sum(nodes, K):
    i, j = 0, len(nodes) - 1
    while i < j:
        sum = nodes[i] + nodes[j]
        if sum == K:
            return (nodes[i], nodes[j])
        elif sum < K:
            i += 1
        else:
            j -= 1