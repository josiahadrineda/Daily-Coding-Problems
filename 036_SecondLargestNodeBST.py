class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, node):
        if not root:
            root = node
        else:
            if node.val < root.val:
                if not root.left:
                    root.left = node
                else:
                    self.insert(root.left, node)
            else:
                if not root.right:
                    root.right = node
                else:
                    self.insert(root.right, node)
    
    def second_largest(self, root):
        def inorder(arr, root):
            if root:
                inorder(arr, root.left)
                arr.append(root.val)
                inorder(arr, root.right)
        
        arr = []
        inorder(arr, root)

        print("Inorder traversal of BST:", arr)
        print("Second largest element in BST:", arr[-2])

        return arr[-2]

#Driver code
bst = BST()
bst.root = Node(5)

bst.insert(bst.root, Node(1))
bst.insert(bst.root, Node(2))
bst.insert(bst.root, Node(3))
bst.insert(bst.root, Node(4))
bst.insert(bst.root, Node(6))
bst.insert(bst.root, Node(7))
bst.insert(bst.root, Node(8))
bst.insert(bst.root, Node(9))

bst.second_largest(bst.root)