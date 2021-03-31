def next_greatest_int(n):
    """Given a positive integer N, returns the next greatest integer based on N's
    binary representation.

    >>> next_greatest_int(6)   # 110 -> 1001
    9
    >>> next_greatest_int(21)  # 10101 -> 10110
    22
    """
    assert n > 0, 'N must be a positive integer.'

    def next_greatest_bin(b):
        # [s, e)
        def fill(l, s, e, d):
            l[s:e] = [d] * (e - s)

        l = list(b)
        n = len(l)

        i = n - 1
        while l[i] != '1':
            i -= 1
        i -= 1
        while i >= 0 and l[i] == '1':
            i -= 1

        if i < 0:
            c = l.count('1')
            l.append('#')
            fill(l, 0, n + 1, '0')
            l[0] = '1'
            fill(l, n - c + 2, n + 1, '1')
        else:
            l[i], l[i + 1] = l[i + 1], l[i]
            c = l[i + 2:].count('1')
            fill(l, i + 1, n, '0')
            fill(l, n - c + 1, n, '1')
        return ''.join(l)

    b = str(bin(n))[2:]
    res_b = next_greatest_bin(b)
    res = int(res_b, 2)
    return res