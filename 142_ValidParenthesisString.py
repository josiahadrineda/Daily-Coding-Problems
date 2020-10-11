def check_valid_string(s):
    """Given a string containing only three types of characters:
    '(', ')', and '*', determines whether the parentheses are
    balanced. '*' can be treated as '(', ')', or an empty string.

    >>> check_valid_string('')
    True
    >>> check_valid_string('(()*')
    True
    >>> check_valid_string('(*)')
    True
    >>> check_valid_string('*(*()*()*')
    True
    >>> check_valid_string('*))')
    False
    """
    if not s:
        return True

    min_pair, max_pair = 0, 0
    for char in s:
        # ( or *
        max_pair = max_pair - 1 if char == ')' else max_pair + 1
        # ) or *
        min_pair = min_pair + 1 if char == '(' else max(min_pair - 1, 0)
        # Check for incongruencies
        if max_pair < 0:
            return False
    return min_pair == 0