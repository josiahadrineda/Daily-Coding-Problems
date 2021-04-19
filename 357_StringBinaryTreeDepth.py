def depth(tree):
    """Given a string representation of a Binary Tree TREE, return its depth. A node
    in TREE is represented by (lr), where l is the node's left child and r is the
    node's right child. If either of a node's children is None, it will be represented
    as a 0.

    >>> depth('(00)')   # A root node with no children
    0
    >>> depth('((00)(00))') # A root node with two children
    1
    >>> depth('((((00)0)0)0)') # An unbalanced tree with three consecutive left children
    3
    """
    assert tree, 'TREE cannot be an empty string.'

    res, curr = 0, 0
    for c in tree:
        if c == '(':
            curr += 1
        elif c == ')':
            curr -= 1
        res = max(res, curr)
    return res - 1