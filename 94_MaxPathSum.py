class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

def max_path_sum(root):
    max_path_sum_helper.res = float('-inf')
    max_path_sum_helper(root)
    return max_path_sum_helper.res if max_path_sum_helper.res != float('-inf') else 0

def max_path_sum_helper(root):
    if not root:
        return 0

    l = max_path_sum_helper(root.left)
    r = max_path_sum_helper(root.right)

    max_path_from_root = max(max(l, r) + root.val, root.val)

    tot_max_path = max(max_path_from_root, l + r + root.val)
    max_path_sum_helper.res = max(max_path_sum_helper.res, tot_max_path)

    return max_path_from_root

tree = Tree()
assert max_path_sum(tree.root) == 0

tree = Tree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
assert max_path_sum(tree.root) == 11

tree = Tree()
tree.root = Node(-1)
tree.root.left = Node(-2)
tree.root.right = Node(3)
tree.root.left.left = Node(-4)
tree.root.left.right = Node(5)
assert max_path_sum(tree.root) == 5