# https://github.com/vineetjohn/daily-coding-problem/blob/master/solutions/problem_248.py
# I would have never thought of this btw...

def max(a, b):
    """Finds the max of two integers A and B without if/else statements,
    branching, or direct comparisons.

    >>> max(2, 1)
    2
    >>> max(2, 2)
    2
    >>> max(2, 3)
    3
    """
    assert type(a) == int, 'A must be an integer.'
    assert type(b) == int, 'B must be an integer.'

    diff = a - b
    sign = (diff >> 31) & 1
    return a - sign * diff