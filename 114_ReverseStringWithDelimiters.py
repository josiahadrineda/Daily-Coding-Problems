def reverse_string_w_delims(S):
    """
    Given a string S and a set of delimiters,
    reverses the words in S while maintaining
    the relative order of the delimiters.

    >>> reverse_string_w_delims('hello/world:here')
    'here/world:hello'
    >>> reverse_string_w_delims('hello/world:here/')
    'here/world:hello/'
    >>> reverse_string_w_delims('hello//world:here')
    'here//world:hello'
    >>> reverse_string_w_delims('//.,::')
    '//.,::'
    >>> reverse_string_w_delims('/a/b/c/d/e/f/g/h/')
    '/h/g/f/e/d/c/b/a/'
    """
    assert S, 'Cannot reverse an empty string.'

    separated_S = []
    switch = 0
    for char in S:
        if char.isalpha():
            if not separated_S or not switch:
                separated_S.append(char)
                switch = 1
            elif switch:
                separated_S[-1] += char
        else:
            if not separated_S or switch:
                separated_S.append(char)
                switch = 0
            elif not switch:
                separated_S[-1] += char

    i, j = 0, len(separated_S)-1
    while i < j:
        while i < j and not separated_S[i].isalpha():
            i += 1
        while j > i and not separated_S[j].isalpha():
            j -= 1
        separated_S[i], separated_S[j] = separated_S[j], separated_S[i]
        i, j = i + 1, j - 1
    
    return ''.join(separated_S)