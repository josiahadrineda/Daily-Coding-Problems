def sum_set_bits(n):
    """Given a positive integer N, returns the total number of set bits from numbers
    1 ... N.

    >>> sum_set_bits(69)
    205
    """
    assert n > 0, 'N must be a positive integer.'

    bits = [0]
    while len(bits) <= n:
        for bit in list(bits):
            bits.append(bit + 1)
    return sum(bits[:n+1])