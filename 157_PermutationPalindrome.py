def permutation_palindrome(s):
    """Given a string S, determines whether any permutation of
    S is a valid palindrome.

    >>> permutation_palindrome('carrace')
    True
    >>> permutation_palindrome('daily')
    False
    """
    assert s, 'Cannot find any permutations of empty string.'

    if s == s[::-1]:
        return True

    freq = {}
    for char in s:
        if not freq.get(char):
            freq[char] = 0
        freq[char] += 1

    odds = [k for k,v in freq.items() if v % 2 == 1]
    return len(odds) <= 1