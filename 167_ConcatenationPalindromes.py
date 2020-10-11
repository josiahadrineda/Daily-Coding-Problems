# https://fizzbuzzed.com/top-interview-questions-5/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.palindromes_below = []
        self.ind = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, ind, word):
        root = self.root
        for i, char in enumerate(reversed(word)):
            if is_palindrome(word[:len(word)-i]):
                root.palindromes_below.append(ind)
            if not root.children.get(char):
                root.children[char] = TrieNode()
            root = root.children[char]
        root.ind = ind

    def find_palindromes(self, prefix):
        root = self.root
        inds = []
        for i, char in enumerate(prefix):
            if root.ind is not None:
                if is_palindrome(prefix[i:]):
                    inds.append(root.ind)
            if not root.children.get(char):
                return inds
            root = root.children[char]

        if root.ind is not None:
            inds.append(root.ind)
        inds.extend(root.palindromes_below)
        return inds

def concatenate_palindromes(words):
    """Given a list of WORDS, finds all pairs of unique indices such that
    the concatenation of the two words is a palindrome.

    >>> concatenate_palindromes(['abcd', 'dcba', 'lls', 's', 'sssll'])
    [(0, 1), (1, 0), (2, 4), (3, 2)]
    >>> concatenate_palindromes(['code', 'edoc', 'da', 'd'])
    [(0, 1), (1, 0), (2, 3)]
    """
    assert words, 'Cannot find any palindromes within an empty list.'

    trie = Trie()
    for i, word in enumerate(words):
        trie.add_word(i, word)

    res = []
    for i, word in enumerate(words):
        inds = trie.find_palindromes(word)
        res.extend([(i, ind) for ind in inds if i != ind])
    return res

def is_palindrome(word):
    return word == word[::-1]