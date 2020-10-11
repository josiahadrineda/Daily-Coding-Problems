class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def evaluate(root):
    if str(root.val) in '+-*/':
        if root.val == '+':
            return evaluate(root.left) + evaluate(root.right)
        elif root.val == '-':
            return evaluate(root.left) - evaluate(root.right)
        elif root.val == '*':
            return evaluate(root.left) * evaluate(root.right)
        elif root.val == '/':
            return evaluate(root.left) / evaluate(root.right)
    else:
        return root.val

expression = Node('*', Node('+', Node(3), Node(2)), Node('+', Node(4), Node(5)))
assert evaluate(expression) == 45