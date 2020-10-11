def reverse(lst, i, j):
    """Reverses a list LST from index I to index J.
    """
    assert lst, 'Cannot reverse an empty list.'
    assert 0 <= i < len(lst), 'Index I out of bounds.'
    assert 0 <= j < len(lst), 'Index J out of bounds.'
    assert i <= j, 'Index I must be less than or equal to index J.'

    return lst[:i] + lst[i:j+1][::-1] + lst[j+1:]

# O(n^2)

def sort_via_reverse(lst):
    """Sorts a list LST using only the reverse function implementation.

    >>> sort_via_reverse([1, 8, 7, 4, 6, 2, 5, 3, 0, 9])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    if not lst or len(lst) == 0:
        return []
    elif len(lst) == 1:
        return lst

    """
    Two-step Operation

    1. find smallest element in lst
    2. reverse said element to front of list
    *repeat process for list[1:] until completely sorted*
    """

    for i in range(len(lst)-1):
        min_el = min(lst[i:])
        ind = lst[i:].index(min_el)
        if lst[i] == min_el:
            continue
        else:
            lst = reverse(lst, i, ind+i)
    return lst