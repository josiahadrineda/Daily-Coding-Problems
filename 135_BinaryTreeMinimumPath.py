class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        if not self:
            return ''
        s = f'Node({self.val}'
        if self.left:
            s += f', {repr(self.left)}'
        if self.right:
            s += f', {repr(self.right)}'
        s += ')'
        return s

class Tree:
    def __init__(self):
        self.root = None

    def __repr__(self):
        return repr(self.root)

    def min_sum_path(self):
        def min_sum_backtrack(root, curr, path_sums):
            if not root.left and not root.right:
                path_sums.append(curr)
            else:
                for child in root.left, root.right:
                    if child:
                        curr += child.val
                        path_sums = min_sum_backtrack(child, curr, path_sums)
                        curr -= child.val
            return path_sums
        
        if not self.root:
            return 0

        path_sums = min_sum_backtrack(self.root, self.root.val, [])
        return min(path_sums)

t = Tree()
t.root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
assert repr(t) == 'Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))'
assert t.min_sum_path() == 7