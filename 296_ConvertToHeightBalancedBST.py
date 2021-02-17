class BSTNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def _is_height_balanced(self):
        return self.__is_height_balanced_recur() > 0

    def __is_height_balanced_recur(self):
        if not self:
            return 0
        
        lh = self.left.__is_height_balanced_recur() if self.left else 0
        if lh == -1:
            return -1
        rh = self.right.__is_height_balanced_recur() if self.right else 0
        if rh == -1:
            return -1
        
        if abs(lh - rh) > 1:
            return -1
        return 1 + max(lh, rh)

    def __repr__(self):
        res = f'Node({self.val}'
        if self.left:
            res += f', {repr(self.left)}'
        if self.right:
            res += f', {repr(self.right)}'
        res += ')'
        return res

class BST:
    def __init__(self, root=None):
        self.root = root

    def is_height_balanced(self):
        return self.root._is_height_balanced() if self.root else False

    def __repr__(self):
        return repr(self.root)

def convert_to_height_balanced_bst(nums):
    """Given a SORTED list of integers NUMS, converts NUMS into a height-balanced
    binary search tree.

    >>> nums = [1, 2, 3, 4, 5, 6, 7]
    >>> t1 = convert_to_height_balanced_bst(nums)
    >>> t1.is_height_balanced()
    True
    >>> t1
    Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
    >>> nums = [1, 2, 3, 4]
    >>> t2 = convert_to_height_balanced_bst(nums)
    >>> t2.is_height_balanced()
    True
    >>> t2
    Node(2, Node(1), Node(3, Node(4)))
    """
    assert nums, 'NUMS cannot be an empty list.'

    def convert_recur(nums):
        if not nums:
            return None
        elif len(nums) == 1:
            return BSTNode(nums[0])
        else:
            l, r = 0, len(nums) - 1
            m = l + (r - l) // 2
            node = BSTNode(nums[m])
            node.left = convert_recur(nums[l:m])
            node.right = convert_recur(nums[m+1:r+1])
            return node

    t = BST()
    t.root = convert_recur(nums)
    return t