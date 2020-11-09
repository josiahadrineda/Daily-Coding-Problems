class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root = None

def most_frequent_subtree_sum(root):
    """Given the root of a binary tree ROOT, returns the most frequent
    subtree sum. If there is a tie, return all sums with the highest
    frequency in any order.

    >>> t = Tree()
    >>> t.root = Node(5, Node(2), Node(-5))
    >>> most_frequent_subtree_sum(t.root)
    [2]
    >>> t2 = Tree()
    >>> t2.root = Node(5, Node(2), Node(-3))
    >>> sorted(most_frequent_subtree_sum(t2.root))
    [-3, 2, 4]
    """
    
    """
    1. Calculate the subtree sum for every node in tree (store in list)
    2. Return most frequent element in said list
    """

    def find_subtree_sums(node):
        if not node:
            return 0
        elif not node.left or not node.right:
            sums.append(node.val)
            return node.val
        else:
            l, r = find_subtree_sums(node.left), find_subtree_sums(node.right)
            s = l + r + node.val

            sums.append(s)
            return s

    sums = []
    find_subtree_sums(root)

    freq = {}
    for s in sums:
        freq[s] = freq.get(s, 0) + 1
    
    global_max, local_max = 0, 0
    for v in freq.values():
        if v > local_max:
            local_max = v
        global_max = max(global_max, local_max)

    return [k for k,v in freq.items() if v == global_max]