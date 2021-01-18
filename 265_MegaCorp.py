def pay_employees(work):
    """Given a list of hours worked by every employee in MegaCorp WORK, pay them
    according to this rule: every employee should be given the smallest positive
    amount, and employees who work more than their neighbor should be given more.

    >>> pay_employees([10, 40, 200, 1000, 60, 30])
    [1, 2, 3, 4, 2, 1]
    >>> pay_employees([10, 40, 200, 1000, 60, 30, 20])
    [1, 2, 3, 4, 3, 2, 1]
    >>> pay_employees([50, 40, 30, 20, 10, 20, 30, 40, 30, 20, 30, 40, 50])
    [5, 4, 3, 2, 1, 2, 3, 4, 2, 1, 2, 3, 4]
    >>> pay_employees([50, 60, 50, 70, 70])
    [1, 2, 1, 2, 2]
    """
    assert work, 'WORK cannot be an empty list.'

    def get_segments(work):
        if work[1] > work[0]:
            dir = 1
        elif work[1] == work[0]:
            dir = 0
        else:
            dir = -1
        prev, start = work[0], 0

        segments = []
        for i, w in enumerate(work[1:]):
            if dir == 1 and w <= prev:
                segments.append((dir, i - start + 1))
                start = i + 1
                if w < prev:
                    dir = -1
                else:
                    dir = 0
            elif dir == 0 and w != prev:
                segments.append((dir, i - start + 1))
                start = i + 1
                if w > prev:
                    dir = 1
                else:
                    dir = -1
            elif dir == -1 and w >= prev:
                segments.append((dir, i - start + 1))
                start = i + 1
                if w > prev:
                    dir = 1
                else:
                    dir = 0
            prev = w
        segments.append((dir, len(work) - start))
        return segments

    segments = get_segments(work)

    res = []
    for dir, len_seg in segments:
        if dir == 1:
            seg = list(range(1, len_seg + 1))
            if res and res[-1] == seg[0]:
                seg = [s + 1 for s in seg]
        elif dir == 0:
            seg = [res[-1]] * len_seg
        else:
            seg = reversed(list(range(1, len_seg + 1)))
        res.extend(seg)
    return res