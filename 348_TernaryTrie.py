class TTrieNode:
    def __init__(self, val=None):
        self.val = val
        self.children = [None] * 3
        self.is_end = False

    def get_left_child(self):
        return self.children[0]

    def get_middle_child(self):
        return self.children[1]

    def get_right_child(self):
        return self.children[2]

    def set_left_child(self, node):
        self.children[0] = node

    def set_middle_child(self, node):
        self.children[1] = node

    def set_right_child(self, node):
        self.children[2] = node

class TTrie:
    """A Trie represented by a Ternary Search Tree.

    **Note: Assume that only LOWERCASE words are used as input.**

    >>> tt = TTrie()
    >>> tt.insert('code')
    >>> tt.insert('cob')
    >>> tt.search('code')
    True
    >>> tt.search('cob')
    True
    >>> tt.search('cod')
    False
    >>> tt.insert('be')
    >>> tt.insert('bee')
    >>> tt.search('bee')
    True
    >>> tt.search('be')
    True
    >>> tt.search('b')
    False
    >>> tt.insert('ax')
    >>> tt.insert('war')
    >>> tt.insert('we')
    >>> tt.search('we')
    True
    """

    def __init__(self):
        self.root = TTrieNode()

    def _binary_search(self, val, node, parent=None):
        if not node:
            return parent
        elif node.val == val:
            return node
        elif val < node.val:
            return self._binary_search(val, node.get_left_child(), node)
        return self._binary_search(val, node.get_right_child(), node)

    def insert(self, word):
        root = self.root
        for c in word:
            node = self._binary_search(c, root.get_middle_child())
            if not node:
                root.set_middle_child(TTrieNode(c))
                node = root.get_middle_child()
            elif c < node.val:
                node.set_left_child(TTrieNode(c))
                node = node.get_left_child()
            elif c > node.val:
                node.set_right_child(TTrieNode(c))
                node = node.get_right_child()
            root = node
        root.is_end = True

    def search(self, word):
        root = self.root
        for c in word:
            node = self._binary_search(c, root.get_middle_child())
            if not node or node.val != c:
                return False
            root = node
        return root.is_end