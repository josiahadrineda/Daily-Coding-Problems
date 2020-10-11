def hops(hop_list):
    """
    Returns whether one can reach the end of a list
    of possible hop values.

    >>> hops([2, 0, 1, 0])
    True
    >>> hops([5, 0, 0, 0])
    True
    >>> hops([1, 1, 0, 1])
    False
    """
    assert len(hop_list) > 0, 'Cannot have a negative or empty hop list.'

    return hops_backtrack(hop_list, 0)

def hops_backtrack(hop_list, ind):
    if ind >= len(hop_list) - 1:
        return True
    elif hop_list[ind] == 0:
        return False
    else:
        for i in range(1, hop_list[ind]+1):
            if hops_backtrack(hop_list, ind+i):
                return True
        return False