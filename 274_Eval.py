def evaluate(expr):
    """Given a string consisting of parentheses, single digits, and positive and negative
    signs EXPR, converts EXPR into a mathematical expression to obtain the answer.

    **Note: Assume EXPR is always valid.**

    >>> evaluate('-1 + ( 2 + 3 )')
    4
    >>> evaluate('1+2-3+4-5')
    -1
    """
    assert expr, 'EXPR cannot be an empty string.'

    expr = expr.replace('(', ' ').replace(')', ' ').replace('+', ' ')

    tokens = []
    i = 0
    while i < len(expr):
        char = expr[i]
        if char == ' ':
            pass
        elif char == '-':
            tokens.append(expr[i:i+2])
            i += 1
        else:
            tokens.append(char)
        i += 1
    return sum([int(t) for t in tokens])