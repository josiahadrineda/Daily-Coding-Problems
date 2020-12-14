from functools import lru_cache

def rearrange(s):
    """Given a string with repeated characters S, rearranges S so that no
    two adjacent characters are the same. If not possible, returns None.

    >>> rearrange('aaaaabbbc')
    'abababaca'
    >>> rearrange('aaab')
    """
    assert s, 'S cannot be an empty string.'

    def is_valid(s):
        return s[0] != s[1] and s[-1] != s[-2]

    @lru_cache(maxsize=None)
    def rearrange_recur(s, curr):
        if not s:
            return curr
        elif not curr:
            return rearrange_recur(s[1:], s[0])
        else:
            for i in range(len(s)):
                first, rest = s[i], s[:i] + s[i+1:]
                if is_valid(curr + first):
                    cand = rearrange_recur(rest, curr + first)
                    if cand: return cand
                if is_valid(first + curr):
                    cand = rearrange_recur(rest, first + curr)
                    if cand: return cand
            return None
    return rearrange_recur(s, '')