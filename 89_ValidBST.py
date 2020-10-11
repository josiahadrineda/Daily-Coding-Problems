class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return 'Val:{}\tLeftL{}\tRightL{}\n'.format(self.val, self.left, self.right)

class BST:
    def __init__(self):
        self.root = None

    def __repr__(self):
        nodes = []
        q = [self.root]
        if not q:
            return nodes

        while q:
            curr = q.pop(0)
            nodes.append(curr.val)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return 'Nodes: ' + str(nodes)

def valid_bst(root):
    if not root or (not root.left and not root.right):
        return True
    elif root.left and not root.right:
        return root.left.val <= root.val and valid_bst(root.left)
    elif root.right and not root.left:
        return root.right.val >= root.val and valid_bst(root.right)
    else:
        return root.left.val <= root.val <= root.right.val and \
               valid_bst(root.left) and valid_bst(root.right)

def valid_bst_cleaner(root):
    return bst_helper(root, -float('inf'), float('inf'))

def bst_helper(root, lo, hi):
    if root and lo <= root.val <= hi:
        return bst_helper(root.left, lo, root.val) and \
               bst_helper(root.right, root.val, hi)
    return not root

bst = BST()
bst.root = Node(0)
bst.root.left = Node(-1)
bst.root.left.left = Node(-2)
bst.root.left.right = Node(0)
bst.root.right = Node(1)
bst.root.right.left = Node(0)
bst.root.right.right = Node(2)
print(bst)

assert valid_bst(bst.root)

bst = BST()
bst.root = Node(0)
bst.root.left = Node(-3)
bst.root.left.left = Node(-2)
bst.root.left.right = Node(0)
bst.root.right = Node(1)
bst.root.right.left = Node(0)
bst.root.right.right = Node(3)
print(bst)

assert not valid_bst_cleaner(bst.root)