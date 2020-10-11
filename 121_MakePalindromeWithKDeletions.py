def make_palindrome_with_k_deletions(s, k):
    """
    Given a string s, returns whether or not you can make
    a palindrome using at MOST k character deletions.

    >>> make_palindrome_with_k_deletions('waterrfetawx', 2)
    True
    >>> make_palindrome_with_k_deletions('waterrfetawx', 1)
    False
    >>> make_palindrome_with_k_deletions('waterretaw', 0)
    True
    """
    assert s, 'Cannot determine palindromic qualities with an empty string.'
    assert k >= 0, 'Cannot make negative deletions.'

    if k == 0:
        return s == s[::-1]

    l = longest_palindromic_subsequence(s)
    n = len(s) - l

    return k >= n

def longest_palindromic_subsequence(s):
    """
    Given a string s, returns the longest palindromic
    subsequence within s.

    >>> longest_palindromic_subsequence('bbbab')
    4
    >>> longest_palindromic_subsequence('cbbd')
    2
    """
    assert s, 'Cannot find longest palindromic subsequence of empty string.'

    def lcs(s, s_rev):
        if not s or not s_rev:
            return 0
        elif s[-1] == s_rev[-1]:
            return 1 + lcs(s[:-1], s_rev[:-1])
        return max(lcs(s[:-1], s_rev), lcs(s, s_rev[:-1]))
    return lcs(s, s[::-1])