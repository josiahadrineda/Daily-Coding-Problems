def nearest_larger_number(arr, i):
    """Given an array of numbers ARR and an index I, returns the index
    of the nearest larger number of the number at index I, where distance
    is measured in array indices.

    >>> nearest_larger_number([4, 1, 3, 5, 6], 0)
    3
    >>> nearest_larger_number([4, 1, 3, 5, 6], 4)
    """
    assert arr, 'No larger integer in empty array.'

    target = arr[i]
    l, r = i, i
    while True:
        if l == 0 and r == len(arr) - 1:
            return None
        else:
            if l - 1 >= 0:
                l -= 1
            if r + 1 <= len(arr) - 1:
                r += 1

            if arr[l] > target:
                return l
            elif arr[r] > target:
                return r