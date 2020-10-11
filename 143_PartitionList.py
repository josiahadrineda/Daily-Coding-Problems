def partition(x, lst):
    """Given a pivot X and a list LST, partitions the list into three parts.
    1 contains all elements in LST that are less than X
    2 contains all elements in LST that are equal to X
    3 contains all elements in LST are are greater than X

    >>> partition(10, [9, 12, 3, 5, 14, 10, 10])
    [3, 9, 5, 10, 10, 14, 12]
    """
    assert lst, 'Cannot partition empty list.'

    arr = lst.copy()
    i = 0
    l, r = 0, len(arr) - 1
    while i < len(arr):
        if arr[i] < x and l < i:
            arr[i], arr[l] = arr[l], arr[i]
            l += 1
        elif arr[i] > x and r > i:
            arr[i], arr[r] = arr[r], arr[i]
            r -= 1
        else:
            i += 1
    return arr