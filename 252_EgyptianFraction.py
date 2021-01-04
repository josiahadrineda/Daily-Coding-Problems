def egyptian_fraction(numer, denom):
    """Breaks a fraction NUMER / DENOM into an Egyptian Fraction, aka a
    sum of smaller fractions whose numerators are all 1.

    >>> egyptian_fraction(3, 17)
    '1/6 + 1/102'
    >>> egyptian_fraction(4, 13)
    '1/4 + 1/18 + 1/468'
    """
    assert numer > 0, 'NUMER must be a positive integer.'
    assert denom > 0, 'DENOM must be a positive integer.'
    assert numer < denom, 'NUMER must be less than DENOM.'

    fractions = []
    curr, i = numer / denom, 2
    while curr > 1e-10:
        while 1 / i > curr:
            i += 1
        curr -= 1 / i
        fractions.append(f'1/{i}')
    return ' + '.join(fractions)