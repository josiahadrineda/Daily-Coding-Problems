from math import floor, ceil

def rounded_array(arr):
    """Given an array of floats ARR, where ARR[i] can be rounded up or down, returns a
    corresponding array of integers that satisfies the following properties:

    1. The rounded sums of both arrays should be equal
    2. The absolute pairwise difference between elements (|x1 - y1| + |x2 - y2| + ... +
       |xn - yn|) is minimized

    >>> rounded_array([1.3, 2.3, 4.4])
    [1, 2, 5]
    >>> rounded_array([1.5, 2.5, 3.5, 4.5])
    [2, 3, 3, 4]
    """
    assert arr, 'ARR cannot be an empty list.'

    def rounded_recur(i, curr, tot, diff):
        if i == n:
            return (curr, diff) if tot == s else ([], float('inf'))
        else:
            f, c = floor(arr[i]), ceil(arr[i])
            f_arr, f_diff = rounded_recur(i + 1, curr + [f], tot + f, diff + abs(arr[i] - f))
            c_arr, c_diff = rounded_recur(i + 1, curr + [c], tot + c, diff + abs(arr[i] - c))
            return (f_arr, f_diff) if f_diff < c_diff else (c_arr, c_diff)

    n, s = len(arr), int(sum(arr))
    return rounded_recur(0, [], 0, 0)[0]