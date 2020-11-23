from functools import lru_cache

def longest_common_subsequence(s, t, u):
    """Given three strings S, T, and U, returns the length of the longest
    common subsequence among S, T, and U.

    >>> s = 'epidemiologist'
    >>> t = 'refrigeration'
    >>> u = 'supercalifragilisticexpialodocious'
    >>> longest_common_subsequence(s, t, u)
    5
    >>> longest_common_subsequence('abc', 'bcd', 'cde')
    1
    """
    assert s, 'S cannot be an empty string.'
    assert t, 'T cannot be an empty string.'
    assert u, 'U cannot be an empty string.'

    @lru_cache(maxsize=None)
    def get_subsequence(s, t, u):
        if not s or not t or not u:
            return 0
        elif s[0] == t[0] == u[0]:
            return 1 + get_subsequence(s[1:], t[1:], u[1:])
        else:
            ones = max(get_subsequence(s[1:], t, u), get_subsequence(s, t[1:], u), get_subsequence(s, t, u[1:]))
            twos = max(get_subsequence(s[1:], t[1:], u), get_subsequence(s, t[1:], u[1:]), get_subsequence(s[1:], t, u[1:]))
            return max(ones, twos)
    return get_subsequence(s, t, u)