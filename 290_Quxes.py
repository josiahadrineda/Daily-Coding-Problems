def quxes(quxes):
    """On a mysterious island there are creatures known as Quxes which come in three
    colors: red, green, and blue. One power of the Qux is that if two of them are
    standing next to each other, they can transform into a single creature of the
    third color. Given N Quxes standing in a line QUXES, determines the smallest
    number of them remaining after any possible sequence of such transformations.

    >>> quxes(['r', 'g', 'b', 'g', 'b'])
    1
    >>> quxes(['r', 'g', 'b'])
    2
    """
    assert quxes, 'QUXES cannot be an empty list.'

    def other(q1, q2):
        colors = ['r', 'g', 'b']
        colors.remove(q1)
        colors.remove(q2)
        return colors

    def quxes_recur(quxes):
        res = float('inf')
        for i, q1 in enumerate(quxes[:-1]):
            q2 = quxes[i + 1]
            if q1 != q2:
                res = min(res, quxes_recur(quxes[:i] + other(q1, q2) + quxes[i+2:]))
        return min(res, len(quxes))
    return quxes_recur(quxes)