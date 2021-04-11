VOWELS = {'a', 'e', 'i', 'o', 'u', 'y', 'w', 'h'}

CONSONANTS_TO_DIGITS = {
    'b': '1', 'f': '1', 'p': '1', 'v': '1',
    'c': '2', 'g': '2', 'j': '2', 'k': '2', 'q': '2', 's': '2', 'x': '2', 'z': '2',
    'd': '3', 't': '3',
    'l': '4',
    'm': '5', 'n': '5',
    'r': '6'
}

def soundex(w):
    """Given an alphabetical word W, implements the Soundex algorithm - an algorithm
    mapping W to a string of one character and three integers 0 - 6 such that two
    words W1 and W2 that sound similar will be given the same mapping (phonetic
    categorization). Soundex is implemented in this manner:

    1. Remove consecutive consonants with the same sound ('ck' -> 'c')
    2. Keep the first letter. The remaining steps only apply to the rest of W
    3. Remove all vowels, including 'y', 'w', and 'h'
    4. Replace all consonsnts with the digits as listed in CONSONANTS_TO_DIGITS
    5. Add zeroes until the mapping has three digits. If more than three digits are
       present, only keep the first three

    >>> soundex('Jackson')
    'J250'
    >>> soundex('Jackson') == soundex('Jaxen')
    True
    >>> soundex('Robert')
    'R163'
    >>> soundex('Robert') == soundex('Rupert')
    True
    >>> soundex('Rubin')
    'R150'
    >>> soundex('Ashcraft')
    'A226'
    >>> soundex('Ashcraft') == soundex('Ashcroft')
    True
    >>> soundex('Tymczak')
    'T522'
    >>> soundex('Pfister')
    'P236'
    >>> soundex('Honeyman')
    'H555'
    """
    assert w, 'W cannot be an empty string.'

    w = w.lower()
    l = list(w)

    f = l[0]

    i, prev = 0, None
    while i < len(l):
        c = l[i]
        if i > 0 and c in VOWELS:
            l[i] = '-1'
        else:
            try:
                l[i] = CONSONANTS_TO_DIGITS[c]
                c = l[i]

                if prev and prev == c != '-1':
                    l.pop(i)
                    c = prev
            except KeyError as e:
                i += 1
        prev = c

    l[0] = f
    l = [c for c in l if c != '-1']

    d = len(l) - 1
    if d < 3:
        l.extend(['0'] * (3 - d))
    
    return ''.join(l[:4]).upper()