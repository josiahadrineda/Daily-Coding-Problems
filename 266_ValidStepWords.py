def valid_step_words(words, word):
    """Given a list of words WORDS and an input_word WORD, returns all valid
    step words from WORD, where a step word is defined as a word that is an anagram
    of WORD after adding one more letter to WORD.

    >>> valid_step_words(['appeal', 'apples', 'approve', 'apricot', 'alpine'], 'apple')
    ['appeal', 'apples']
    """
    assert words, 'WORDS cannot be an empty list.'
    assert word, 'WORD cannot be an empty string.'

    def is_valid(w, word):
        if len(w) != len(word) + 1:
            return False

        for c in word:
            try:
                w.remove(c)
            except Exception as e:
                return False
        return len(w) == 1

    res = []
    for w in words:
        if is_valid(list(w), word):
            res.append(w)
    return res