SEPARATORS = {',', ';', ':'}
TERMINAL_MARKS = {'.', '?', '!'}
SPECIAL_CHARS = SEPARATORS | TERMINAL_MARKS
SPECIAL_CHARS.add(' ')

def is_valid_sentence(sentence):
    """Given a string SENTENCE, determines whether SENTENCE is valid based on the
    following rules:

    1. SENTENCE must start with a capital letter, followed by a lowercase letter or a space.
    2. All other characters must be lowercase letters, separators, or terminal marks.
    3. There must be a single space between each word.
    4. SENTENCE must end with a terminal mark immediately following a word.

    >>> is_valid_sentence("The quick brown, fox jumped; over the: lazy dog!")
    True
    >>> is_valid_sentence("Hello world!?")
    False
    >>> is_valid_sentence("i am a giraffe")
    False
    >>> is_valid_sentence("Ugly;barnacle.")
    False
    """
    assert sentence, 'SENTENCE cannot be an empty string.'

    n = len(sentence) - 1
    for i in range(len(sentence)):
        char = sentence[i]
        if i == 0 and char.upper() != char:
            return False
        elif i > 0 and char not in SPECIAL_CHARS and char.upper() == char:
            return False

        if i < n and char in TERMINAL_MARKS:
            return False
        elif i == n and char not in TERMINAL_MARKS:
            return False

        if char in SEPARATORS and sentence[i + 1] != ' ':
            return False
    return True