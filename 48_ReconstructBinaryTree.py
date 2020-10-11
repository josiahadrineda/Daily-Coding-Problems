"""
preorder = root, left, right
inorder = left, root, right
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def preorder(root):
    if root:
        print(root.val, end=' ')
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        preorder(root.left)
        print(root.val, end=' ')
        preorder(root.right)

def reconstruct(preorder, inorder):
    if inorder:
        ind = inorder.index(preorder.pop(0))
        node = Node(inorder[ind])
        node.left = reconstruct(preorder, inorder[:ind])
        node.right = reconstruct(preorder, inorder[ind+1:])
        return node

preord = ['a', 'b', 'd', 'e', 'c', 'f', 'g']
inord = ['d', 'b', 'e', 'a', 'f', 'c', 'g']

reconstructed_tree = reconstruct(preord, inord)
preorder(reconstructed_tree)
print()
inorder(reconstructed_tree)