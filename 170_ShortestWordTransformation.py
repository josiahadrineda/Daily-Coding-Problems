def shortest_word_transformation(start, end, words):
    """Given a START word, and END word, and a list of words WORDS,
    returns the shortest transformation sequence from START to END such that
    only one letter is changed at each step of the sequence, and each
    transformed word exists in WORDS. If no such sequence exists,
    None is returned.

    >>> words = ['dot', 'dop', 'dat', 'cat']
    >>> shortest_word_transformation('dog', 'cat', words)
    ['dog', 'dot', 'dat', 'cat']
    >>> words = ['dot', 'dop', 'dat', 'dar']
    >>> shortest_word_transformation('dog', 'cat', words)
    """
    assert words, 'WORDS cannot be an empty list.'

    if end not in words:
        return None
    else:
        res = shortest_word_backtrack(start, end, words, [])
        if res:
            return [start] + res

def shortest_word_backtrack(start, end, words, curr):
    if start == end:
        return curr
    else:
        for ind, word in enumerate(words):
            if is_valid(start, word):
                curr.append(word)
                words.pop(ind)

                res = shortest_word_backtrack(word, end, words, curr)
                if res:
                    return res

                curr.pop()
                words.insert(ind, word)

def is_valid(word1, word2):
    mismatches = 0
    for char1, char2 in zip(word1, word2):
        mismatches += (char1 != char2)
    return mismatches == 1