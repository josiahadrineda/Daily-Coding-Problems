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

def print_paths(root):
    """
    Given a binary tree, prints all paths
    from the root to leaves.

    >>> t = Tree()
    >>> t.root = Node(1, Node(2), Node(3, Node(4), Node(5)))
    >>> print_paths(t.root)
    [[1, 2], [1, 3, 4], [1, 3, 5]]
    """
    assert root, 'Cannot print paths for an empty tree.'

    return paths_backtrack(root, [], [])

def paths_backtrack(root, paths, curr_path):
    """
    A helper function for print_paths.
    """

    if not root.left and not root.right:
        paths.append(curr_path.copy() + [root.val])
    else:
        curr_path.append(root.val)
        for child in root.left, root.right:
            paths_backtrack(child, paths, curr_path)
        curr_path.pop()
    return paths