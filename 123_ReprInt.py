def repr_int(s):
    """
    Given a string s, returns whether it
    represents a number.

    >>> repr_int('10')
    True
    >>> repr_int('-10')
    True
    >>> repr_int('10.1')
    True
    >>> repr_int('-10.1')
    True
    >>> repr_int('1e5')
    True
    >>> repr_int('-1e5')
    True
    >>> repr_int('a')
    False
    >>> repr_int('x 1')
    False
    >>> repr_int('a -2')
    False
    >>> repr_int('-')
    False
    """
    assert type(s) == str, 's must be a valid string literal.'

    # Test for int
    try:
        x = int(s)
        return True
    except ValueError:
        pass

    # Test for float
    try:
        x = float(s)
        return True
    except ValueError:
        pass

    # Test for scientific notation
    if 'e' in s:
        i = s.index('e')
        return s.count('e') == 1 and s.count('.') == 0 and \
            repr_int(s[:i]) and repr_int(s[i+1:])

    return False