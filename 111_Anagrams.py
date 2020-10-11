from collections import defaultdict

def anagrams(W, S):
    """
    Given a word W and a string S, finds all
    starting indices in S which are anagrams of W.

    >>> anagrams('ab', 'abxaba')
    [0, 3, 4]
    """
    assert W and S, 'W and/or S must not be empty strings.'

    inds = []
    w, s = len(W), len(S)
    for s, e in zip(range(s - w+1), range(w, s+1)):
        if is_anagram(W, S[s:e]):
            inds.append(s)
    return inds

def is_anagram(W, seg):
    W_freqs = count_frequencies(W)
    seg_freqs = count_frequencies(seg)
    return W_freqs == seg_freqs

def count_frequencies(word):
    d = defaultdict(int)
    for char in word:
        d[char] += 1
    return d


def more_efficient_anagrams(W, S):
    """
    More efficient version of the above anagrams algorithm.

    >>> more_efficient_anagrams('ab', 'abxaba')
    [0, 3, 4]
    """
    assert W and S, 'W and/or S must not be empty strings.'

    w = len(W)

    W_freqs = count_frequencies(W)
    curr_S_freqs = {}

    inds = []
    cnt = 0
    for ind, char in enumerate(S):
        # This is the point where we have to start removing chars
        # in order to stay within the bounds of W.
        if cnt == w:
            curr_S_freqs[S[ind - w]] -= 1
            if curr_S_freqs[S[ind - w]] == 0:
                del curr_S_freqs[S[ind - w]]
        else:
            cnt += 1

        # Updating curr_S_freq dict with each new char occurrence.
        if not curr_S_freqs.get(char):
            curr_S_freqs[char] = 0
        curr_S_freqs[char] += 1

        # An anagram has been found!
        if curr_S_freqs == W_freqs:
            inds.append(ind - w+1)
    return inds