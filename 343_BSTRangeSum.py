from math import ceil, log2
from bisect import bisect_right

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root = None

    def _inorder(self):
        def inorder_recur(root):
            if root:
                inorder_recur(root.left)
                nodes.append(root.val)
                inorder_recur(root.right)
        
        nodes = []
        inorder_recur(self.root)
        return nodes

# https://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/
class SegmentTree:
    """Constructs a Segment Tree given a Binary Search Tree BST. Supports get_sum
    and update operations (cannot add or remove values).

    >>> t = Tree()
    >>> t.root = Node(5, Node(3, Node(2), Node(4)), Node(8, Node(6), Node(10)))
    >>> st = SegmentTree(t)
    >>> st.get_sum(4, 9)
    23
    >>> st.update(10, 12)
    >>> st.get_sum(0, 12)
    40
    """

    def __init__(self, bst):
        self.nodes = bst._inorder()
        self.n = len(self.nodes)
        self.h = ceil(log2(self.n))
        self.seg_tree = [None] * (2 * 2**self.h - 1)

        self._construct_seg_tree(0, self.n - 1, 0)

    def _construct_seg_tree(self, s, e, i):
        if s == e:
            self.seg_tree[i] = self.nodes[s]
        else:
            m = s + (e - s) // 2
            self.seg_tree[i] = self._construct_seg_tree(s, m, 2 * i + 1) \
                            + self._construct_seg_tree(m + 1, e, 2 * i + 2)
        return self.seg_tree[i]

    def get_sum(self, s_val, e_val):
        def sum_recur(s, e, qs, qe, i):
            if s > qe or e < qs:
                return 0
            elif s >= qs and e <= qe:
                return self.seg_tree[i]
            else:
                m = s + (e - s) // 2
                return sum_recur(s, m, qs, qe, 2 * i + 1) \
                     + sum_recur(m + 1, e, qs, qe, 2 * i + 2)

        lb, ub = bisect_right(self.nodes, s_val) - 1, bisect_right(self.nodes, e_val) - 1
        return sum_recur(0, self.n - 1, lb, ub, 0)

    def update(self, old_val, new_val):
        def update_recur(s, e, t, diff, i):
            if t < s or t > e:
                return

            self.seg_tree[i] += diff
            if s != e:
                m = s + (e - s) // 2
                update_recur(s, m, t, diff, 2 * i + 1)
                update_recur(m + 1, e, t, diff, 2 * i + 2)

        diff = new_val - old_val
        target = bisect_right(self.nodes, old_val) - 1
        self.nodes[target] = new_val
        return update_recur(0, self.n - 1, target, diff, 0)