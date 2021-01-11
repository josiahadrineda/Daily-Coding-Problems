class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        if not self.left and not self.right:
            return f'Node({self.val})'
        elif self.left and not self.right:
            return f'Node({self.val}, Node({repr(self.left)}))'
        elif not self.left and self.right:
            return f'Node({self.val}, Node({repr(self.right)}))'
        else:
            return f'Node({self.val}, Node({repr(self.left)}), Node({repr(self.right)}))'

class Tree:
    def __init__(self):
        self.root = None
    
    def __repr__(self):
        return repr(self.root)

def boustrophedon(t):
    """Given a binary tree T, traverses T in "boustrophedon" order,
    where "boustrophedon" is an Ancient Greek style of reading, where
    the first line is read from left to right, the second from right to
    left, and so on and so forth (like a snake-like pattern).

    >>> t = Tree()
    >>> t.root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
    >>> boustrophedon(t)
    [1, 3, 2, 4, 5, 6, 7]
    >>> t.root = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    >>> boustrophedon(t)
    [1, 2, 3, 4, 5]
    """
    assert t, 'T cannot be an empty binary tree.'

    levels = {}
    q = [(t.root, 0)]
    while q:
        curr, level = q.pop(0)
        if curr.left:
            q.append((curr.left, level + 1))
        if curr.right:
            q.append((curr.right, level + 1))
        
        if levels.get(level) == None:
            levels[level] = []
        levels[level].append(curr.val)
    
    for k in levels.keys():
        if k % 2 == 1:
            levels[k] = levels[k][::-1]

    return sum(levels.values(), [])