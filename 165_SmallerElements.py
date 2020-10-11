"""https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76657/3-ways-(Segment-Tree-Binary-Indexed-Tree-Binary-Search-Tree)-clean-python-code"""

class SegmentTreeNode:
    def __init__(self, val, start, end):
        self.val = val
        self.start = start
        self.end = end
        self.children = []

class SegmentTree:
    def __init__(self, n):
        self.root = self.build(0, n-1)

    def __repr__(self):
        self.print_nodes(self.root)
        return ''

    def print_nodes(self, root, indent=0):
        if root:
            whitespace = '   ' * indent
            print(whitespace + str((root.val, root.start, root.end)))
            for child in root.children:
                self.print_nodes(child, indent+1)

    def build(self, start, end):
        if start > end:
            return

        root = SegmentTreeNode(0, start, end)
        if start == end:
            return root

        mid = start + (end - start) // 2
        root.children = [
            self.build(start, end)
            for start, end in ((start, mid), (mid+1, end))
        ]

        return root

    def update(self, i, val, root=None):
        root = root or self.root
        if i < root.start or i > root.end:
            pass
        elif i == root.start == root.end:
            root.val += val
        else:
            root.val = sum([
                self.update(i, val, child)
                for child in root.children
            ])

        return root.val

    def sum(self, start, end, root=None):
        root = root or self.root
        if end < root.start or start > root.end:
            return 0
        elif start <= root.start and end >= root.end:
            return root.val
        else:
            return sum([
                self.sum(start, end, child)
                for child in root.children
            ])

def smaller_elements(nums):
    """Given an array of integers NUMS, returns a new array where
    each element in said array is the number of smaller elements
    to the right of that element in NUMS.

    >>> smaller_elements([3, 4, 9, 6, 1])
    [1, 1, 2, 1, 0]
    """
    assert nums, 'Cannot determine smaller elements in empty array.'

    num_dict = {num: ind for ind, num in enumerate(sorted(set(nums)))}
    
    seg_tree, res = SegmentTree(len(num_dict)), []
    for i in range(len(nums)-1, -1, -1):
        res.append(seg_tree.sum(0, num_dict[nums[i]]-1))
        seg_tree.update(num_dict[nums[i]], 1)
    return res[::-1]