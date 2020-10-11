def smallest_distance(w1, w2, words):
    """Given two words W1 and W2 as well as a string of words WORDS,
    returns the shortest distance between W1 and W2. Distance is defined
    as the number of words between W1 and W2.

    >>> smallest_distance('hello', 'world', 'dog cat hello cat dog dog hello cat world')
    1
    """
    assert w1, 'W1 cannot be an empty string.'
    assert w2, 'W2 cannot be an empty string.'
    assert words, 'WORDS cannot be an empty string.'
    assert w1 in words and w2 in words, 'Cannot find distance if W1 and/or W2 is/are not in WORDS.'

    min_dist, w1_ind, w2_ind = float('inf'), None, None
    for ind, word in enumerate(words.split()):
        if word == w1:
            w1_ind = ind
        elif word == w2:
            w2_ind = ind

        if w1_ind and w2_ind:
            min_dist = min(min_dist, abs(w2_ind - w1_ind - 1))
    return min_dist