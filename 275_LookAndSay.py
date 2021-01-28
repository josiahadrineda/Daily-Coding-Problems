def look_and_say(n):
    """Given a positive integer N, return the Nth term in the "look and say" sequence,
    where each subsequent term visually describes the digits appearing in the previous
    term.

    >>> for i in range(1, 11):
    ...     print(look_and_say(i))
    1
    11
    21
    1211
    111221
    312211
    13112221
    1113213211
    31131211131221
    13211311123113112211
    """
    assert n > 0, 'N must be a positive integer.'

    res = str(1) + '#'
    for _ in range(n - 1):
        new_res = ''
        prev, freq = None, 0
        for char in res:
            if prev != char:
                if prev:
                    new_res += str(freq) + prev
                freq = 0
            prev, freq = char, freq + 1
        res = new_res + '#'
    return res[:-1]