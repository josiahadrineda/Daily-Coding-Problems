"""
Follow-ups:
 - What if transitive relationships hold? Union Find.
 - What if phrases can be used as synonyms? Iterate char by char (as opposed to word
   by word) until a discrepancy is found, then recurse over all possibilities until
   proven equivalent (or exhausted all options).
 - What if equivalence is affected by punctuation? The only relevant punctuation marks
   are sentence dividers such as commas (,), hyphens (-), colons (:) and semicolons(;),
   so treat them as words when iterating.
"""

PUNCTUATION = ",-:;.!?'\""

def equivalent(synonyms, s1, s2):
    """Given a set of synonyms in the format (word1, word2) SYNONYMS and two sentences
    of equal length S1 and S2, determines whether S1 is equivalent to S2.

    **Note: (a, b) and (a, c) does NOT imply (a, c). Also assume that equivalence is
    NOT affected by punctuation.**

    >>> synonyms = set([('big', 'large'), ('eat', 'consume')])
    >>> equivalent(synonyms, 'He wants to eat food.', 'He wants to consume food.')
    True
    >>> equivalent(synonyms, 'That is one big tree!', 'That is one large tree...')
    True
    >>> equivalent(synonyms, 'That - is one big tree!', 'That, is one large tree!?')
    True
    >>> equivalent(synonyms, 'I ate an apple.', 'I consumed an apple.')
    False
    """
    assert synonyms, 'SYNONYMS cannot be an empty set.'
    assert s1, 'S1 cannot be an empty string.'
    assert s2, 'S2 cannot be an empty string.'

    def remove_punctuation(w):
        while w and w[0] in PUNCTUATION:
            w = w[1:]
        while w and w[-1] in PUNCTUATION:
            w = w[:-1]
        return w

    s = {}
    for a,b in synonyms:
        s[a] = s.get(a, set()) | set([b])
        s[b] = s.get(b, set()) | set([a])

    ws1, ws2 = s1.split(), s2.split()
    ws1 = [remove_punctuation(w) for w in ws1]
    ws1 = [w for w in ws1 if w != '']
    ws2 = [remove_punctuation(w) for w in ws2]
    ws2 = [w for w in ws2 if w != '']

    for w1, w2 in zip(ws1, ws2):
        if w1 == w2:
            continue
        if (w1 in s and w2 in s[w1]) or (w2 in s and w1 in s[w2]):
            continue
        return False
    return True