def reverse_bits(n):
    """Given a 32-bit integer N, returns the number with its bits reversed.

    >>> reverse_bits(2863311530) # 1010 1010 1010 1010 1010 1010 1010 1010 --> 0101 0101 0101 0101 0101 0101 0101 0101
    1431655765
    >>> reverse_bits(4042322160) # 1111 0000 1111 0000 1111 0000 1111 0000 --> 0000 1111 0000 1111 0000 1111 0000 1111
    252645135
    """
    assert 0 <= n < 2**32 - 1, 'N must be a 32-bit integer.'

    bin_n = convert_to_bin(n)
    bin_n = bin_n[::-1]
    res = convert_from_bin(bin_n)

    return res

def convert_to_bin(n):
    bin_n = ''
    while n:
        n, rem = n // 2, n % 2
        bin_n = str(rem) + bin_n
    return bin_n

def convert_from_bin(bin_n):
    n, exp = 0, 0
    while bin_n:
        bin_n, last = bin_n[:-1], bin_n[-1]
        n, exp = n + int(last) * 2**exp, exp + 1
    return n