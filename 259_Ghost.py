class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        root = self.root
        for c in word:
            if root.children.get(c) == None:
                root.children[c] = TrieNode()
            root = root.children[c]
        root.is_end = True

def ghost(words):
    """Given a list of words WORDS, determines the letters for which, when
    played optimally, will guarantee a win in a game of "Ghost".

    "Ghost" is a two-person word game where players alternate appending
    letters to a word. The first person who spells out a word, or creates
    a prefix for which there is no possible continuation, loses.

    >>> sorted(ghost(['cat', 'calf', 'dog', 'bear']))
    ['b']
    >>> sorted(ghost(['ca', 'cal']))
    ['c']
    """
    assert words, 'WORDS cannot be an empty list.'

    def play(root, c):
        """Determines whether any play will result in a win (True)
        given starting character C.
        """

        def play_recur(node, player_turn=True):
            if node.is_end:
                return not player_turn
            elif len(node.children) > 1:
                return player_turn
            return play_recur(list(node.children.values())[0], not player_turn)

        return play_recur(root.children[c])

    t = Trie()
    for word in words:
        t.add_word(word)

    root = t.root
    res = []
    for c in sorted(root.children.keys()):
        if play(root, c):
            res.append(c)
    return res