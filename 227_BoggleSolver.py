# Only self-critique: TOO MANY PARAMS !!!

ADJ_COORDS = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def add_word(self, word):
        curr = self
        for char in word:
            if not curr.children.get(char):
                curr.children[char] = Trie()
            curr = curr.children[char]
        curr.is_end = True

def boggle_solver(board, dictionary):
    """Given a list of lists BOARD representing a game board of Boggle, as well as
    a set of words DICTIONARY that represents all available words given BOARD,
    "solves" BOARD.

    >>> board = [
    ...     ["A", "L", "B", "P"],
    ...     ["C", "O", "E", "Y"],
    ...     ["F", "C", "H", "P"],
    ...     ["B", "A", "D", "A"]
    ... ]
    >>> words_in_board = {
    ...     "AFOCAL", "CHAPEL", "CLOCHE", "DHOLE", "LOCHE", "CHOLA", "CHELA",
    ...     "HOLEY", "FOCAL", "FOLEY", "COLEY", "COLBY", "COHAB", "COBLE", "DACHA",
    ...     "BACHA", "BACCO", "BACCA", "BLECH", "PHOCA", "ALOHA", "ALEPH", "CHAPE",
    ...     "BOCCA", "BOCCE", "BOCHE", "LECH", "PECH", "OCHE", "FOAL", "YECH", "OBEY",
    ...     "YEBO", "LOCA", "LOBE", "LOCH", "HYPE", "HELO", "PELA", "HOLE", "COCA"
    ... }
    >>> words_not_in_board = {
    ...     "DUMMY", "WORDS", "FOR", "TESTING"
    ... }
    >>> dictionary = words_in_board | words_not_in_board
    >>> found_words = boggle_solver(board, dictionary)
    >>> found_words == words_in_board
    True
    """
    assert board, 'BOARD cannot be an empty list.'
    assert dictionary, 'DICTIONARY cannot be an empty set.'

    t = Trie()
    for word in dictionary:
        t.add_word(word)

    found_words = set()
    for i in range(4):
        for j in range(4):
            find_all_words((i,j), set(), t, board, dictionary, '', found_words)
    return found_words

def find_all_words(coord, visited, trie, board, dic, curr, res):
    if trie.is_end:
        res.add(curr)
    if is_valid(coord, visited, trie, board):
        visited.add(coord)
        r, c = coord
        char = board[r][c]
        curr += char
        for adj_coord in ADJ_COORDS:
            r_adj, c_adj = adj_coord
            find_all_words((r + r_adj, c + c_adj), visited, trie.children[char], board, dic, curr, res)
        visited.remove(coord)

def is_valid(coord, visited, trie, board):
    r, c = coord
    return 0 <= r < 4 and 0 <= c < 4 and \
        coord not in visited and trie.children.get(board[r][c])