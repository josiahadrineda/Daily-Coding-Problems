"""
Comments:
 - I generally don't like the idea of allocating a bunch of space to lists (sorted,
   too) every time I find a valid window.
 - If there was an "OrderedSet" that supports indexing, this would be much more
   efficient.
"""

def distinct_char_window(s):
    """Given a string S, computes the length of the smallest window that contains
    every distinct character in S.

    >>> distinct_char_window('jiujitsu')
    5
    >>> distinct_char_window('aaabbbccc')
    5
    """
    assert s, 'S cannot be an empty string.'

    n, l = len(s), len(set(list(s)))

    recent_chars = {}
    res, i = float('inf'), 0
    while i < n:
        while i < n:
            if len(recent_chars) == l:
                items = sorted([(v,k) for k,v in recent_chars.items()])
                inds, chars = [v for v,_ in items], [k for _,k in items]
                lo, hi = inds[0], inds[-1]

                res = min(res, hi - lo + 1)
                recent_chars.pop(chars[inds.index(lo)])

                break
            recent_chars[s[i]] = i
            i += 1
        i += 1
    return res