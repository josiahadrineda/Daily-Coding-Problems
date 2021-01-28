# Knuth-Morris-Pratt (KMP) Algorithm
# https://geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
def string_match(s, p):
    """Given a string S of length N and a pattern P of length k, searches for P in S
    with < O(N * k) worst-case time complexity. If the P is found, returns the start
    index of its location, otherwise returns False.

    >>> string_match('aaaabbbbccccaabbccabc', 'abc')
    18
    >>> string_match('aaaaccccbbbbaaccbbacb', 'abc')
    False
    """
    assert s, 'S cannot be an empty string.'
    assert p, 'P cannot be an empty string.'

    # Longest Prefix (that is also a) Suffix
    def compute_lps(p, k):
        l, i = 0, 1
        lps = [0] * k
        while i < k:
            if p[l] == p[i]:
                l += 1
                lps[i] = l
                i += 1
            else:
                if l:
                    l = lps[l - 1]
                else:
                    lps[i] = l
                    i += 1
        return lps

    n, k = len(s), len(p)
    lps = compute_lps(p, k)

    i, j = 0, 0
    while i < n:
        if s[i] == p[j]:
            i, j = i + 1, j + 1
        if j == k:
            return i - j
        elif i < n and s[i] != p[j]:
            if j:
                j = lps[j - 1]
            else:
                i += 1
    return False