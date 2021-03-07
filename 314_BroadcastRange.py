def min_broadcast_range(listeners, towers):
    """You are the technical director of a radio company. For simplicity's sake,
    consider each listener to live along a horizontal line from 0 - 1000. Given
    a list of listeners' locations LISTENERS as well as a list of radio towers'
    locations TOWERS, determines the minimum broadcast range in order for each
    listener's home to be covered.

    >>> min_broadcast_range([1, 5, 11, 20], [4, 8, 15])
    5
    """
    assert listeners, 'LISTENERS cannot be an empty list.'
    assert towers, 'TOWERS cannot be an empty list.'

    def bisect(arr, x):
        l, r = 0, len(arr) - 1
        while l < r:
            m = l + (r - l) // 2
            if arr[m] == x:
                return m
            elif arr[m] < x:
                l = m + 1
            else:
                r = m - 1
        return l

    listeners.sort()
    towers.sort()

    n = len(listeners)

    res = float('-inf')
    for t in towers:
        i = bisect(listeners, t)
        if i == n:
            bc_range = t - listeners[i - 1]
        elif i == 0:
            bc_range = listeners[i] - t
        elif listeners[i] == t:
            bc_range = 0
        else:
            bc_range = max(listeners[i] - t, listeners[i - 1] - t)
        res = max(res, bc_range)
    return res