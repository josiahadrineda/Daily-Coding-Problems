class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'Val: {}'.format(self.val)

class Tree:
    def __init__(self):
        self.root = None

    def __repr__(self):
        root = self.root
        q = [root]
        nodes = []
        while q:
            curr = q.pop(0)
            nodes.append(curr.val)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return str(nodes)

    def invert(self, root):
        root.right, root.left = root.left, root.right
        if root.left: self.invert(root.left)
        if root.right: self.invert(root.right)

tree = Tree()
tree.root = Node('a')
tree.root.left = Node('b')
tree.root.right = Node('c')
tree.root.left.left = Node('d')
tree.root.left.right = Node('e')
tree.root.right.right = Node('f')
print(tree)

tree.invert(tree.root)
print(tree)