def largest_area_naive(hist):
    """Given a list of positive integers HIST, where HIST[i] corresponds to the height
    of the ith bar of a histogram, computes the area of the largest rectangle that can
    be formed from the bars of HIST.

    >>> largest_area_naive([1, 3, 2, 5])
    6
    """
    assert hist, 'HIST cannot be an empty list.'

    n = len(hist)

    res = 0
    for i in range(n):
        for j in range(n):
            w = j - i + 1
            l = float('inf')
            for k in range(i, j + 1):
                l = min(l, hist[k])
            res = max(res, l * w)
    return res

def largest_area_quick(hist):
    """Same as LARGEST_AREA_NAIVE but quicker.

    >>> largest_area_naive([1, 3, 2, 5])
    6
    """
    assert hist, 'HIST cannot be an empty list.'

    n = len(hist)

    first_left, first_right = [0] * n, [0] * n
    first_left[0], first_right[-1] = -1, n

    # For the ith bar, find the index of the first bar to the LEFT of i whose height is
    # smaller than HIST[i]
    for i in range(1, n):
        l = i - 1
        while l >= 0 and hist[l] >= hist[i]:
            l = first_left[l]
        first_left[i] = l

    # For the ith bar, find the index of the first bar to the RIGHT of i whose height is
    # smaller than HIST[i]
    for i in range(n - 2, -1, -1):
        r = i + 1
        while r < n and hist[r] >= hist[i]:
            r = first_right[r]
        first_right[i] = r

    res = 0
    for i in range(n):
        a = hist[i] * (first_right[i] - first_left[i] - 1)
        res = max(res, a)
    return res