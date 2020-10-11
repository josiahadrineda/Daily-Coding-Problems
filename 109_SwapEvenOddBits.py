def swap_even_odd_bits(n):
    """
    Given an unsigned 8-bit integer,
    swaps the even and odd bits.

    ex. (170) 10101010 -> (85) 01010101

    >>> swap_even_odd_bits(170)
    85
    >>> swap_even_odd_bits(226)
    209
    >>> swap_even_odd_bits(27)
    39
    """
    assert n >= 0, 'n must be unsigned, aka non-negative.'
    assert n < 1 << 8, 'n must be an 8-bit integer.'
    assert type(n) == int, 'n must be an integer.'

    b = bin(n)[2:]
    b = '0'*(8-len(b)) + b
    return int(swap_recur(b), 2)

def swap_recur(s):
    if len(s) == 0:
        return s
    return s[1] + s[0] + swap_recur(s[2:])


def swap_one_liner(n):
    # Shift all even and odd bits
    return ((n & 0b10101010) >> 1) | ((n & 0b01010101) << 1)

assert swap_one_liner(170) == 85
assert swap_one_liner(226) == 209
assert swap_one_liner(27) == 39