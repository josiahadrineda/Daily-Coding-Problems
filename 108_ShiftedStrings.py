def is_shift(a, b):
    """
    Returns whether or not string 'a' can be
    shifted to become string 'b'.

    >>> is_shift('abcde', 'cdeab')
    True
    >>> is_shift('abc', 'acb')
    False
    """
    assert a, "'a' cannot be an empty string."
    assert b, "'b' cannot be an empty string."

    # O(1)
    return len(a) == len(b) and a in 2*b

    # O(n)
    """for _ in range(len(a)):
        a = a[-1] + a[:-1]
        if a == b:
            return True
    return False"""