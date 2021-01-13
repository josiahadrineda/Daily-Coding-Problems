class TrieNode:
    def __init__(self, val='*'):
        self.val = val
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, val, word):
        root = self.root
        for char in word:
            if root.children.get(char) == None:
                root.children[char] = TrieNode()
            root = root.children[char]
        root.val = val

def build_huffman_tree(mappings):
    """Given a dictionary of mappings MAPPINGS, where each k: v pair is a
    char: binary string, creates a Trie (Huffman Tree) storing said mappings.
    """
    assert mappings, 'MAPPINGS must be a valid dictionary.'

    t = Trie()
    for char, b_str in mappings.items():
        t.add_word(char, b_str)
    return t

def decode_binary_string(huffman_tree, b_str):
    """Given a Huffman Tree HUFFMAN_TREE and a binary string B_STR, returns
    the character that B_STR maps to.

    >>> huffman_tree = build_huffman_tree({'a': '01', 'c': '000', 's': '111', 't': '10'})
    >>> chars = []
    >>> chars.append(decode_binary_string(huffman_tree, '000'))
    >>> chars.append(decode_binary_string(huffman_tree, '01'))
    >>> chars.append(decode_binary_string(huffman_tree, '10'))
    >>> chars.append(decode_binary_string(huffman_tree, '111'))
    >>> ''.join(chars)
    'cats'
    """
    assert huffman_tree, 'HUFFMAN_TREE must be a valid Huffman Tree.'
    assert b_str, 'B_STR must be a valid string.'

    root = huffman_tree.root
    for char in b_str:
        root = root.children[char]
    return root.val