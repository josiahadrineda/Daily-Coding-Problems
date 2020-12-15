class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, key, value):
        root = self.root
        while key:
            first, key = key[0], key[1:]
            if not root.children.get(first):
                root.children[first] = TrieNode()
            root = root.children[first]
        root.val = value

    def prefix_sum(self, prefix):
        def sum_all_values(root):
            return root.val + sum([sum_all_values(child) for child in root.children.values()])

        root = self.root
        while prefix:
            first, prefix = prefix[0], prefix[1:]
            if not root.children.get(first):
                return 0
            root = root.children[first]
        return sum_all_values(root)

class PrefixMapSum:
    """A dictionary that has the ability to sum values whose keys have the same prefix.

    >>> pms = PrefixMapSum()
    >>> pms.sum("col")
    0
    >>> pms.insert("columnar", 3)
    >>> pms.sum("col")
    3
    >>> pms.insert("column", 2)
    >>> pms.sum("col")
    5
    """

    def __init__(self):
        self.prefix_map = Trie()

    def insert(self, key, value):
        assert type(key) == str, 'KEY must be a string.'
        assert type(value) == int, 'KEY must be an integer.'
        self.prefix_map.add_word(key, value)

    def sum(self, prefix):
        assert type(prefix) == str, 'PREFIX must be a string.'
        return self.prefix_map.prefix_sum(prefix)