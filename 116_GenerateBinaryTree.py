from random import random

# Eager eval
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def print_all_nodes(self, root, indent=0):
        tab = ' ' * indent
        if root:
            print(tab + str(root.val))
            self.print_all_nodes(root.left, indent + 1)
            self.print_all_nodes(root.right, indent + 1)

def generate_eager():
    """
    Generates a finite, but arbitrarily large
    binary tree in O(1)
    """
    root = Node(0)

    if random() > 0.5:
        root.left = generate()
    if random() > 0.5:
        root.right = generate()

    return root

"""for _ in range(3):
    root = generate_eager()
    root.print_all_nodes(root)"""


# Lazy eval
class LNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self._left = left
        self._right = right

        self._is_left_eval = False
        self._is_right_eval = False

    def print_all_nodes(self, root, indent=0):
        tab = ' ' * indent
        if root:
            print(tab + str(root.val))
            self.print_all_nodes(root.left, indent + 1)
            self.print_all_nodes(root.right, indent + 1)

    @property
    def left(self):
        if not self._is_left_eval:
            if random() > 0.5:
                self._left = LNode(0)

        self._is_left_eval = True
        return self._left

    @property
    def right(self):
        if not self._is_right_eval:
            if random() > 0.5:
                self._right = LNode(0)

        self._is_right_eval = True
        return self._right

def generate_lazy():
    """
    The quicker version of generate_eager()
    """
    return LNode(0)

for i in range(10):
    print(f'Tree #{i+1}:')
    root = generate_lazy()
    root.print_all_nodes(root)
    print()

"""
Thoughts:
- Can this really be considered O(1)?
- Isn't this just generating the tree on demand?
"""