def reverse_string(s):
    """
    Given a string of words delimited by spaces,
    reverses the words in the string.

    >>> reverse_string('hello world here')
    'here world hello'
    """
    assert s, 's cannot be an empty string.'

    return ' '.join(s.split()[::-1])