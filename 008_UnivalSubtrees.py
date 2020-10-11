import time
def display_and_runtime(f):
    def get_display_and_runtime(*args, **kwargs):
        s = time.time()
        print("Solution for {}: {}".format(f.__name__, f(*args, **kwargs)))
        e = time.time()
        print("Runtime for {}: {}s".format(f.__name__, e-s))

        print()
        return
    return get_display_and_runtime

class Node:
    def __init__(self, left=None, right=None, val=None):
        self.left = left
        self.right = right
        self.val = val

def insert(root, node):
    if root is None:
        root = node
    else:
        queue = []
        queue.append(root)

        while queue:
            temp = queue.pop(0)
            if temp.left is None:
                temp.left = node
                break
            else:
                queue.append(temp.left)

            if temp.right is None:
                temp.right = node
                break
            else:
                queue.append(temp.right)

@display_and_runtime
def get_num_subtrees_topdown(root):
    def is_unival(root):
        return unival_helper(root, root.val)

    def unival_helper(root, value):
        if root is None:
            return True
        if root.val == value:
            return unival_helper(root.left, value) and unival_helper(root.right, value)
        return False

    def count_num_univals(root):
        if root is None:
            return 0
        l = count_num_univals(root.left)
        r = count_num_univals(root.right)
        return l+r+1 if is_unival(root) else l+r

    return count_num_univals(root)

@display_and_runtime
def get_num_subtrees_bottomup(root):
    def count_num_univals(root):
        count, _ = helper(root)
        return count

    def helper(root):
        if root is None:
            return 0, True

        get_left_subtrees, is_left_unival = helper(root.left)
        get_right_subtrees, is_right_unival = helper(root.right)
        tot = get_left_subtrees + get_right_subtrees

        if is_left_unival and is_right_unival:
            if root.left and root.val != root.left.val:
                return tot, False
            if root.right and root.val != root.right.val:
                return tot, False
            return tot+1, True
        return tot, False

    return count_num_univals(root)

#Driver code
unival = Node(None)

import random
for i in range(10000):
    insert(unival, Node(val=random.randint(0, 1)))

get_num_subtrees_topdown(unival)
get_num_subtrees_bottomup(unival)