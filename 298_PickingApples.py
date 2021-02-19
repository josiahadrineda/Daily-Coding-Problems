def longest_path(apples, k=2):
    """Given a list representing a row of different types of apples APPLES, returns the
    length of the longest path containing K types of apples.

    >>> longest_path([2, 1, 2, 3, 3, 1, 3, 5])
    4
    """
    assert apples, 'APPLES cannot be an empty list.'
    assert k > 0, 'K must be a positive integer.'

    apples = ''.join([str(a) for a in apples])

    recent_apples, curr_apples, curr_apples_str = {}, set(), ''
    res = 0
    for i,a in enumerate(apples):
        recent_apples[a] = i
        curr_apples.add(a)
        curr_apples_str += a
        if len(curr_apples) == k:
            res = max(res, len(curr_apples_str))
        elif len(curr_apples) > k:
            to_remove, remove_ind = '', float('inf')
            for cand in curr_apples:
                if recent_apples[cand] < remove_ind:
                    to_remove = cand
                    remove_ind = recent_apples[cand]
            curr_apples.remove(to_remove)
            curr_apples_str = apples[remove_ind+1:i+1]
    return res