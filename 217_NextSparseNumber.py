# nishantnaveen.wordpress.com/2016/03/06/finding-next-sparse-number/

def next_sparse_number(n):
    """Given a positive integer N, finds the smallest sparse number greater than
    or equal to N, where a sparse number is defined as a number whose binary
    representation contains no adjacent ones.

    >>> next_sparse_number(21)
    21
    >>> next_sparse_number(22)
    32
    """
    assert n > 0, 'N must be a positive integer.'

    ref, copy, cnt = n, n, 0
    while copy:
        if (copy & 3) == 3:
            n += 1 << cnt
            copy = n >> cnt
        cnt += 1
        copy >>= 1

    if n == ref:
        return n
    else:
        copy, cnt = n, 0
        while copy:
            if (copy & 1) == 1:
                temp = n ^ (1 << cnt)
                if temp > ref:
                    n = temp
                else:
                    break
            copy >>= 1
            cnt += 1
        return n