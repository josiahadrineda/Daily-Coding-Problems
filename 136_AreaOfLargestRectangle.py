def largest_rectangle(matrix):
    """Given an N by M matrix consisting of only ones and zeroes, finds
    the largest rectangle containing only ones and returns its area.

    >>> largest_rectangle([[1,0,0,0],
    ...                    [1,0,1,1],
    ...                    [1,0,1,1],
    ...                    [0,1,0,0]])
    4
    >>> largest_rectangle([[1,0,0,0],
    ...                    [1,1,1,1],
    ...                    [1,1,1,1],
    ...                    [0,1,0,0]])
    8
    """
    assert matrix, 'No rectangle in empty matrix.'

    res = 0
    hist = [0] * len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == 0:
                hist[j] == matrix[i][j]
            else:
                if matrix[i-1][j] == matrix[i][j] == 1:
                    hist[j] += 1
                else:
                    hist[j] = matrix[i][j]
        res = max(res, max_area_from_hist(hist))
    return res

def max_area_from_hist(hist):
    """Calculates the maximum area rectangle from histogram hist,
    where hist is a list whose elements correspond to bar heights.

    >>> max_area_from_hist([1,1,1,1,1])
    5
    >>> max_area_from_hist([1,2,3,2,1])
    6
    """
    assert hist, 'Cannot calculate area from empty histogram.'

    stack = [-1]
    hist.append(0)
    res = 0
    for i, bar in enumerate(hist):
        while hist[stack[-1]] > bar:
            l = hist[stack.pop()]
            w = i - stack[-1] - 1
            res = max(res, l * w)
        stack.append(i)
    hist.pop()
    return res