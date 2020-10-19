def character_mapping(s1, s2):
    """Given two strings S1 and S2, returns whether there is a one-to-one
    character mapping between said strings.

    >>> character_mapping('abc', 'bcd')
    True
    >>> character_mapping('foo', 'baa')
    True
    >>> character_mapping('foo', 'bar')
    False
    """
    assert s1, 'S1 must be a valid string.'
    assert s2, 'S2 must be a valid string.'

    mapping = {}
    for c1, c2 in zip(s1, s2):
        if mapping.get(c1):
            if mapping[c1] != c2:
                return False
        else:
            mapping[c1] = c2
    return True