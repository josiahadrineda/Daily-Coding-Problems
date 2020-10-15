def word_concatenation_indices(s, words):
    """Given a string S and a list of words WORDS, where each word in
    words is the same length, returns all starting indices of substrings
    in S that is a concatenation of every word in WORDS exactly once.

    >>> word_concatenation_indices('dogcatcatcodecatdog', ['cat', 'dog'])
    [0, 13]
    >>> word_concatenation_indices('barfoobazbitbyte', ['cat', 'dog'])
    []
    """
    assert s, 'S cannot be an empty string.'
    assert words, 'WORDS cannot be an empty list'

    words = set(words)
    n, m = len(s), len(''.join(words))
    if n < m:
        return []

    freq_words = freq_counter(words)
    reset = freq_words[:]
    inds, s_so_far = [], ''

    for ind, char in enumerate(s):
        freq_words[ord(char) - 97] -= 1
        if freq_words[ord(char) - 97] < 0:
            freq_words, s_so_far = reset[:], ''
            continue
            
        s_so_far += char
        if len(s_so_far) == m:
            if not all(freq_words):
                if check(s_so_far, set(words)):
                    inds.append(ind - m + 1)
            freq_words[ord(char) - 97] += 1
            s_so_far = s_so_far[1:]

    return inds

def freq_counter(it):
    freqs = [0] * 26
    for elem in it:
        for el in elem:
            freqs[ord(el) - 97] += 1
    return freqs

def check(s, words):
    if not s:
        return not words
    else:
        s_so_far = ''
        for ind, char in enumerate(s):
            s_so_far += char
            if s_so_far in words:
                words.remove(s_so_far)
                if check(s[ind+1:], words):
                    return True
                words.add(s_so_far)
        return False