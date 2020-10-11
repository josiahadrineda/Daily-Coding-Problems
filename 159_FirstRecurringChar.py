def first_recurring_char(s):
    """Given a string S, returns the first recurring character in S
    if present, otherwise returns None.

    >>> first_recurring_char('acbbac')
    'b'
    >>> first_recurring_char('abcdef')
    """
    assert s, 'Cannot search an empty string.'

    visited = set()
    for char in s:
        if char in visited:
            return char
        visited.add(char)
    return None