# This is entirely brute force atm. Sorry, I'm on break rn and I really
# don't feel like doing this rn... make sure to revisit this in the future.

def cryptarithmetic_solver(a, b, c):
    """Given three words A, B, and C, where A + B = C and
    each letter in A, B, and C represents a unique digit,
    solves the equation.

    **Note: The input puzzle should be a valid one.**

    >>> res = cryptarithmetic_solver('SEND', 'MORE', 'MONEY')
    >>> res['D'] == 7
    True
    >>> res['E'] == 5
    True
    >>> res['M'] == 1
    True
    >>> res['N'] == 6
    True
    >>> res['O'] == 0
    True
    >>> res['R'] == 8
    True
    >>> res['S'] == 9
    True
    >>> res['Y'] == 2
    True
    """

    def crypta_backtrack(a, b, c, nums, chars):
        if not chars:
            return int(''.join(a)) + int(''.join(b)) == int(''.join(c))
        else:
            for i, x in enumerate(list(nums)):
                x = str(x)
                replace(a, b, c, chars[0], x)
                if is_valid(a, b, c):
                    res[chars[0]] = int(x)
                    nums.remove(int(x))
                    if crypta_backtrack(a, b, c, nums, chars[1:]):
                        return True
                    nums.insert(i, int(x))
                replace(a, b, c, x, chars[0])

    def replace(a, b, c, x, y):
        for i in range(len(a)):
            if a[i] == x:
                a[i] = y

        for i in range(len(b)):
            if b[i] == x:
                b[i] = y

        for i in range(len(c)):
            if c[i] == x:
                c[i] = y

    def is_valid(a, b, c):
        return a[0] != '0' and b[0] != '0' and c[0] != '0'

    a, b, c = list(a), list(b), list(c)
    res = {}
    crypta_backtrack(a, b, c, list(range(0, 10)), list(set(a + b + c)))

    return res