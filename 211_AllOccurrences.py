def all_occurrences(s, p):
    """Given a string S and a pattern P, finds the starting indices of all
    occurrences of P in S.

    >>> all_occurrences('abracadabra', 'abr')
    [0, 7]
    >>> all_occurrences('aaaaa', 'a')
    [0, 1, 2, 3, 4]
    >>> all_occurrences('aaaaa', 'b')
    []
    """
    assert s, 'S cannot be an empty string.'
    assert p, 'P cannot be an empty string.'

    res = []
    for i in range(len(s)):
        if s[i] == p[0]:
            j, k = i + 1, 1
            while j <= len(s):
                if k == len(p):
                    res.append(i)
                    break
                elif j == len(s) or s[j] != p[k]:
                    break
                j, k = j + 1, k + 1
    return res