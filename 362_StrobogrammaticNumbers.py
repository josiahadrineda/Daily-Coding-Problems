DIGITS = '01689'
REVERSIBLE_DIGITS = '018'

# TC: O(5^N), SC: O(N)
def strobogrammatic_nums(n):
    """A strobogrammatic number is defined as a positive integer that appears the same
    after being rotated 180 degrees, such as the number 16891. Given a positive
    integer N, finds all strobogrammatic numbers with exactly N digits.

    >>> for n in range(1, 11):
    ...     print(len(strobogrammatic_nums(n)))
    3
    4
    12
    20
    60
    100
    300
    500
    1500
    2500
    """
    assert n > 0, 'N must be a positive integer.'

    """
    0
    1
    8
    6 - 9, 9 - 6
    --> [0, 1, 6, 8, 9]

    - Recurse up to (N + 2) // 2 times (basically half the length of the number)
        - Add digit-by-digit into a string
    - If N is odd, 6 and 9 can NOT occupy the middle space
    - Only add to list if len(str(int(current string))) == (N + 2) // 2 (accounts for
      '0')
        - Remember to add the reversal of the current string afterwards
        - Account for 6 - 9, 9 - 6
    """

    def swap(s):
        swapped_s = ''
        for c in s:
            if c == '6':
                swapped_s += '9'
            elif c == '9':
                swapped_s += '6'
            else:
                swapped_s += c
        return swapped_s

    def dfs(dep, curr):
        if dep == 0:
            cand = curr + swap(curr[:-1][::-1]) if n % 2 == 1 else curr + swap(curr[::-1])
            if len(str(int(cand))) == n:
                res.append(int(cand))
        else:
            digits = REVERSIBLE_DIGITS if n % 2 == 1 and dep == 1 else DIGITS
            for d in digits:
                dfs(dep - 1, curr + d)

    half_n, res = (n + 1) // 2, []
    dfs(half_n, '')
    return res

# TC: O(5^N), SC: O(N // 2) --> Faster O(N)
def strobogrammatic_nums_clever(n):
    """Same as above algorithm but clever-er.

    >>> for n in range(1, 11):
    ...     print(len(strobogrammatic_nums(n)))
    3
    4
    12
    20
    60
    100
    300
    500
    1500
    2500
    """

    if n == 0:
        return ['']
    elif n == 1:
        return ['0', '1', '8']
    else:
        res = []
        for strobo_num in strobogrammatic_nums_clever(n - 2):
            res.extend([
                '1' + strobo_num + '1',
                '6' + strobo_num + '9',
                '8' + strobo_num + '8',
                '9' + strobo_num + '8',
            ])
        return res