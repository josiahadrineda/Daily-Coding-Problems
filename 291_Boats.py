def boats(weights, k):
    """Given a list of people's weights WEIGHTS and a maximum weight limit K,
    determines the minimum number of boats needed to accommodate for all people.

    **Note: At most TWO people can fit on one boat at any given time.**

    >>> boats([1, 2], 3)
    1
    >>> boats([3, 2, 2, 1], 3)
    3
    >>> boats([3, 5, 3, 4], 5)
    4
    """
    assert weights, 'WEIGHTS cannot be an empty list.'
    assert k > 0, 'K must be a positive integer.'
    assert max(weights) <= k, 'Biggest person cannot exceed K.'

    weights.sort(reverse=True)

    i, j = 0, len(weights) - 1
    while i <= j:
        if weights[i] + weights[j] <= k:
            j -= 1
        i += 1
    return i