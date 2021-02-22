class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, value):
        root = self.root
        for char in value:
            if root.children.get(char) == None:
                root.children[char] = TrieNode()
            root = root.children[char]
        root.is_end = True

    def search(self, value):
        root = self.root
        for char in value:
            if root.children.get(char) == None:
                return False
            root = root.children[char]
        return root.is_end

class TrieSet:
    """
    An implementation of the Set data structure without resizing the underlying array.
    
    **Note: All values added to the TrieSet must be lowercase.**

    >>> ts = TrieSet()
    >>> ts.add('apple')
    >>> ts.add('anchor')
    >>> ts.add('banana')
    >>> ts.add('cucumber')
    >>> all(ts.check(word) for word in ['apple', 'anchor', 'banana', 'cucumber'])
    True
    >>> ts.check('dumpling')
    False
    """

    def __init__(self):
        self.trie_set = [Trie() for _ in range(26)]

    def _get_ind(self, char):
        return ord(char) - 97

    def add(self, value):
        i = self._get_ind(value[0])
        self.trie_set[i].insert(value)

    def check(self, value):
        i = self._get_ind(value[0])
        return self.trie_set[i].search(value)