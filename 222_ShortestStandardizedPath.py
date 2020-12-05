def shortest_standardized_path(path):
    """Given a string PATH representing an absolute pathname that has .
    and/or .., returns the shortest standardized path.

    >>> shortest_standardized_path('/usr/bin/../bin/./scripts/../')
    '/usr/bin/'
    """
    assert path, 'PATH cannot be an empty string.'

    tokens = path.split('/')[1:-1]
    
    i = 0
    while i < len(tokens):
        if tokens[i] == '..':
            tokens.pop(i - 1)
            tokens.pop(i - 1)
        elif tokens[i] == '.':
            tokens.pop(i)
        else:
            i += 1
    return '/' + '/'.join(tokens) + '/'