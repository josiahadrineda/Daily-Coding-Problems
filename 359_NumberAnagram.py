from random import shuffle

DIGITS_TO_WORDS = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}

def unscramble_number(s):
    """Given a string of concatenated digits ('zero', 'one', 'two', ...) in anagram
    form S, unscrambles S and returns the corresponding number in sorted order.

    **Note: S must be a valid number anagram.**

    >>> unscramble_number('niesevehrtfeev')
    '357'
    >>> unscramble_number(scramble_number('69420'))
    '02469'
    """
    assert s, 'S cannot be an empty string.'

    """
    Exploit the commonalities between digits:

    0 - *z
    1 - (o), n
    2 - *w
    3 - h, (r)
    4 - (f), r
    5 - f, (v)
    6 - s, *x
    7 - (s), v, n
    8 - (h)
    9 - n, (e)
    """

    def remove_digit(f, d, c):
        if d == 0:
            f['z'] = f.get('z', 0) - c
            f['e'] = f.get('e', 0) - c
            f['r'] = f.get('r', 0) - c
            f['o'] = f.get('o', 0) - c
        elif d == 1:
            f['o'] = f.get('o', 0) - c
            f['n'] = f.get('n', 0) - c
            f['e'] = f.get('e', 0) - c
        elif d == 2:
            f['t'] = f.get('t', 0) - c
            f['w'] = f.get('w', 0) - c
            f['o'] = f.get('o', 0) - c
        elif d == 3:
            f['t'] = f.get('t', 0) - c
            f['h'] = f.get('h', 0) - c
            f['r'] = f.get('r', 0) - c
            f['e'] = f.get('e', 0) - 2 * c
        elif d == 4:
            f['f'] = f.get('f', 0) - c
            f['o'] = f.get('o', 0) - c
            f['u'] = f.get('u', 0) - c
            f['r'] = f.get('r', 0) - c
        elif d == 5:
            f['f'] = f.get('f', 0) - c
            f['i'] = f.get('i', 0) - c
            f['v'] = f.get('v', 0) - c
            f['e'] = f.get('e', 0) - c
        elif d == 6:
            f['s'] = f.get('s', 0) - c
            f['i'] = f.get('i', 0) - c
            f['x'] = f.get('x', 0) - c
        elif d == 7:
            f['s'] = f.get('s', 0) - c
            f['e'] = f.get('e', 0) - 2 * c
            f['v'] = f.get('v', 0) - c
            f['n'] = f.get('n', 0) - c
        elif d == 8:
            f['e'] = f.get('e', 0) - c
            f['i'] = f.get('i', 0) - c
            f['g'] = f.get('g', 0) - c
            f['h'] = f.get('h', 0) - c
            f['t'] = f.get('t', 0) - c
        elif d == 9:
            f['n'] = f.get('n', 0) - 2 * c
            f['i'] = f.get('i', 0) - c
            f['e'] = f.get('e', 0) - c

    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1

    n = ''

    # Unique cases
    zs = freq.get('z', 0)
    n += '0' * zs
    remove_digit(freq, 0, zs)

    ws = freq.get('w', 0)
    n += '2' * ws
    remove_digit(freq, 2, ws)

    xs = freq.get('x', 0)
    n += '6' * xs
    remove_digit(freq, 6, xs)

    # Common cases
    ss = freq.get('s', 0)
    n += '7' * ss
    remove_digit(freq, 7, ss)

    vs = freq.get('v', 0)
    n += '5' * vs
    remove_digit(freq, 5, vs)

    fs = freq.get('f', 0)
    n += '4' * fs
    remove_digit(freq, 4, fs)

    rs = freq.get('r', 0)
    n += '3' * rs
    remove_digit(freq, 3, rs)

    hs = freq.get('h', 0)
    n += '8' * hs
    remove_digit(freq, 8, hs)

    os = freq.get('o', 0)
    n += '1' * os
    remove_digit(freq, 1, os)

    es = freq.get('e', 0)
    n += '9' * es
    remove_digit(freq, 9, es)

    return ''.join(sorted(n))

def scramble_number(n):
    s = ''
    for c in n:
        s += DIGITS_TO_WORDS[c]

    l = list(s)
    shuffle(l)
    return ''.join(l)