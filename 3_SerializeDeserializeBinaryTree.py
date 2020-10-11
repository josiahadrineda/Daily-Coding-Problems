class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    """Encodes a tree to a single string.

    :type root: TreeNode
    :rtype: str
    """
    # Layer Order Traversal
    data = ""

    queue = []
    queue.append(root)

    while queue:
        data += str(queue[0].val) + ' '

        node = queue.pop(0)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return data

def deserialize(data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """
    data = data.strip()

    root = Node(None)

    queue = list(data.split(' '))
    while queue:
        val = int(queue.pop(0))
        insert(root, Node(val))
    return root

def insert(root, node):
    if root.val is None:
        root.val = node.val
    else:
        if node.val > root.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


node = Node(3, Node(2, Node(1)), Node(4))
assert deserialize(serialize(node)).left.left.val == 1