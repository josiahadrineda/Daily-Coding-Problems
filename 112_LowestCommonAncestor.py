from collections import defaultdict

class Node:
    def __init__(self, val, parent=None, left=None, right=None):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self):
        print(f'Val: {self.val}')

class Tree:
    def __init__(self):
        self.root = None

    def __repr__(self):
        return str(get_all_nodes(self.root))

def LCA(root, v, w):
    """
    Given a binary tree, finds the lowest common ancestor (LCA)
    of two given nodes in the tree. Each node in the tree also
    has a pointer to its parent.

    >>> t = Tree()
    >>> t.root = Node(3, None, Node(5, None, Node(6), Node(2, None, Node(7), Node(4))), Node(1, None, Node(0), Node(8)))
    >>> t.root.left.parent = t.root.right.parent = t.root
    >>> t.root.left.left.parent = t.root.left.right.parent = t.root.left
    >>> t.root.left.right.left.parent = t.root.left.right.right.parent = t.root.left.right
    >>> t.root.right.left.parent = t.root.right.right.parent = t.root.right
    >>> LCA(t.root, 5, 1)
    3
    >>> LCA(t.root, 0, 4)
    3
    >>> LCA(t.root, 5, 4)
    5
    >>> LCA(t.root, 6, 7)
    5
    """
    assert root, 'Cannot find the LCA of an empty tree.'
    assert is_unique_tree(root), 'All elements of the tree must be unique.'
    assert exists_in_tree(root, v), 'v must exist in the tree.'
    assert exists_in_tree(root, w), 'w must exist in the tree.'
    assert v != w, 'v and w cannot have the same value.'

    # bfs until v or w is found
    # if v is found, trace_ancestry, same for w

    v_ancestry, w_ancestry = [], []
    q = [root]
    while q:
        if v_ancestry and w_ancestry:
            break

        curr = q.pop(0)
        if curr.val == v:
            v_ancestry = trace_ancestry(curr)
        elif curr.val == w:
            w_ancestry = trace_ancestry(curr)

        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)

    # once both v and w ancestries have been traced,
    # it is now simply a matter of finding the smallest indexed similarity

    if len(v_ancestry) <= len(w_ancestry):
        return find_LCA(v_ancestry, set(w_ancestry))
    return find_LCA(w_ancestry, set(v_ancestry))

def trace_ancestry(node):
    nodes = []
    while node:
        nodes.append(node.val)
        node = node.parent
    return nodes

def find_LCA(ancestry1, ancestry2):
    for ancestor in ancestry1:
        if ancestor in ancestry2:
            return ancestor

def is_unique_tree(root):
    """
    Given a binary tree, determines whether all node
    values are unique.

    >>> t = Tree()
    >>> t.root = Node(1, None, Node(2), Node(3))
    >>> is_unique_tree(t.root)
    True
    >>> t.root.left.val = 1
    >>> is_unique_tree(t.root)
    False
    """
    assert root, 'Cannot determine uniqueness with an empty tree.'

    nodes = get_all_nodes(root)
    d = defaultdict(int)
    for node in nodes:
        d[node] += 1
    return all([freq == 1 for freq in d.values()])

def exists_in_tree(root, val):
    """
    Given a binary tree, determines whether the
    given node value is in the tree.

    >>> t = Tree()
    >>> t.root = Node(1, None, Node(2), Node(3))
    >>> exists_in_tree(t.root, 3)
    True
    >>> exists_in_tree(t.root, 4)
    False
    """
    assert root, 'Cannot determine if node value exists in empty tree.'

    nodes = get_all_nodes(root)
    return val in nodes

def get_all_nodes(root):
    if not root:
        return 'Cannot print empty tree.'

    nodes, q = [], [root]
    while q:
        curr = q.pop(0)
        nodes.append(curr.val)
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)
    return nodes