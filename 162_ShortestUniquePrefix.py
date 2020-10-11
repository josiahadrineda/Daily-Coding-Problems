class TrieNode:
    def __init__(self):
        self.freq = 0
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def __repr__(self):
        root = self.root
        self.print_trie(root)
        return ''

    def print_trie(self, root, indent=0):
        for char, child in root.children.items():
            whitespace = '    ' * indent
            print(f'{whitespace}({char}, {child.freq})')
            self.print_trie(child, indent+1)

    def add_word(self, word):
        root = self.root
        for char in word:
            if not root.children.get(char):
                root.children[char] = TrieNode()
            root = root.children[char]
            root.freq += 1

    def unique_prefix(self, word):
        root = self.root
        prefix = ''
        for char in word:
            prefix += char
            root = root.children[char]
            if root.freq == 1:
                break
        return prefix

def shortest_unique_prefix(words):
    """Given a list of WORDS, returns the shortest unique prefix of each word.

    >>> shortest_unique_prefix(['dog', 'cat', 'apple', 'apricot', 'fish'])
    ['d', 'c', 'app', 'apr', 'f']
    """
    assert words, 'No words present in WORDS.'

    trie = Trie()
    for word in words:
        trie.add_word(word)

    prefixes = []
    for word in words:
        prefix = trie.unique_prefix(word)
        prefixes.append(prefix)

    return prefixes