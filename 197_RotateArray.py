def rotate_array(arr, k):
    """Given an array of integers ARR and a positive integer K, rotates
    ARR to the right K elements in-place.

    >>> rotate_array([1, 2, 3, 4, 5], 3)
    [3, 4, 5, 1, 2]
    >>> rotate_array([1, 2, 3, 4, 5] , 5)
    [1, 2, 3, 4, 5]
    """
    assert arr, 'ARR cannot be an empty list.'
    assert k > 0, 'K must be a positive integer.'

    k %= len(arr)
    if not k:
        return arr
    else:
        arr = reverse(arr)
        arr[:k], arr[k:] = reverse(arr[:k]), reverse(arr[k:])
        return arr

def reverse(arr):
    for i in range(len(arr) // 2):
        arr[i], arr[~i] = arr[~i], arr[i]
    return arr