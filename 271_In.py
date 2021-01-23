def in_function(l, x):
    """Given a sorted list of integers L and an integer X, determines whether or not X
    is in L w/o multiplication, division, or bit-shift operations in O(log N) time.

    >>> in_function([1, 2, 3, 3, 5, 7, 7, 9, 10, 13, 15, 16, 17, 18, 20, 20], 15)
    True
    >>> in_function([1, 2, 3, 3, 5, 7, 7, 9, 10, 13, 15, 16, 17, 18, 20, 20], 12)
    False
    """
    assert l, 'L cannot be an empty list.'
    assert type(x) == int, 'X must be an integer.'

    def divide(dividend, divisor):
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0
        while dividend >= divisor:
            dividend -= divisor
            quotient += 1
        return sign * quotient

    lo, hi = 0, len(l) - 1
    while lo <= hi:
        m = lo + divide(hi - lo, 2)
        if l[m] == x:
            return True
        elif l[m] > x:
            hi = m - 1
        else:
            lo = m + 1
    return False