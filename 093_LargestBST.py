class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

def is_valid_bst(root, lb=-float('inf'), ub=float('inf')):
    if root and lb <= root.val <= ub:
        return is_valid_bst(root.left, ub=root.val) and \
               is_valid_bst(root.right, lb=root.val)
    return not root

def count_nodes(root):
    if not root: return 0
    return count_nodes(root.left) + count_nodes(root.right) + 1

def largest_bst(root):
    res = 0
    if not root:
        return res

    q = [root]
    while q:
        curr = q.pop(0)
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)
        res = max(res, count_nodes(curr)) if is_valid_bst(curr) else res
    return res

tree = Tree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(0)
subtree = tree.root.left
subtree.left = Node(1)
subtree.right = Node(3)
assert largest_bst(tree.root) == 3

tree = Tree()
tree.root = Node(1)
tree.root.left = Node(0)
tree.root.right = Node(2)
assert largest_bst(tree.root) == 3

tree = Tree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(0)
assert largest_bst(tree.root) == 1

tree = Tree()
tree.root = None
assert largest_bst(tree.root) == 0