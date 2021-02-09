def kaprekar_steps(n):
    """Given a valid 4-digit number N (at least 2 distinct digits), returns the number
    of steps required to reach Kaprekar's constant. A step consists of finding two
    numbers A and B that are N but sorted in increasing and decreasing order respectively,
    and subtracting A from B.

    >>> kaprekar_steps(1234)
    3
    """
    assert len(str(n)) == 4, 'N must be a 4-digit number.'

    def digitize(n):
        digits = []
        while n:
            n, last = n // 10, n % 10
            digits.append(last)
        return digits

    def numerize(digits):
        res, mul = 0, 1
        while digits:
            last = digits.pop()
            res += last * mul
            mul *= 10
        return res

    def sort_inc(n):
        digits = digitize(n)
        digits.sort()
        return numerize(digits)        

    def sort_dec(n):
        digits = digitize(n)
        digits.sort(reverse=True)
        return numerize(digits)    

    def kaprekar_recur(n, steps):
        if n == 6174:
            return steps
        else:
            a, b = sort_inc(n), sort_dec(n)
            return kaprekar_recur(b - a, steps + 1)
    return kaprekar_recur(n, 0)