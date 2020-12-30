def word_circle(words):
    """Given a list of words WORDS, determines whether the words
    can be rearranged to form a circle. A word X can "connect" to
    another word Y if the last letter of X is the same as the first
    letter of Y.

    >>> word_circle(['chair', 'height', 'racket', 'touch', 'tunic'])
    True
    >>> word_circle(['chair', 'height', 'racket', 'touch'])
    False
    """
    assert words, 'WORDS cannot be an empty list.'

    def word_circle_backtrack(words, curr):
        if not words:
            return len(curr) > 1 and curr[0][0] == curr[-1][-1]
        else:
            for i, word in enumerate(list(words)):
                if is_valid(word, curr):
                    words.remove(word)
                    if word_circle_backtrack(words, curr + [word]):
                        return True
                    words.insert(i, word)
            return False

    def is_valid(word, curr):
        return not curr or curr[-1][-1] == word[0]

    return word_circle_backtrack(words, [])