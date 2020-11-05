def traverse_array(steps):
    """Given a list of nonnegative integers STEPS - representing
    the maximum number of steps one is allowed to traverse from
    that position - determines whether or not traversal from the
    0th index to the (len(steps) - 1)th index is possible.

    >>> traverse_array([1, 0, 0])
    False
    >>> traverse_array([1, 3, 1, 2, 0, 1])
    True
    """
    assert steps, 'STEPS cannot be an empty list.'
    assert all([step >= 0 for step in steps]), 'Step in STEPS should be nonnegative.'

    return traverse_array_backtrack(steps, 0, len(steps) - 1)

def traverse_array_backtrack(steps, s, e):
    if s == e:
        return True
    elif steps[s] == 0:
        return False
    else:
        for step in range(1, steps[s] + 1):
            if traverse_array_backtrack(steps, s + step, e):
                return True
        return False