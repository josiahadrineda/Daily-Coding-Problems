def pyramid(stones):
    """You have N stones in a row, and would like to create from them a pyramid. This
    pyramid should be constructed such that the height of each stone increases by one
    until reaching the tallest stone, after which the heights decrease by one. In
    addition, the start and end stones should each be one stone high. You can pay a
    cost of 1 to lower a stone's height by 1, as many times as necessary. Given a list
    of stone heights STONES, determines the minimum cost to produce a pyramid.

    **Note: A valid pyramid must be able to be constructed from STONES.**

    >>> pyramid([1, 1, 3, 3, 2, 1])
    2
    >>> pyramid([1, 1, 1, 1, 1, 1])
    5
    >>> pyramid([1, 1, 1, 1, 5, 1])
    6
    """
    assert stones, 'STONES cannot be an empty list.'

    def construct_pyramid(n):
        peak = n // 2 + 1
        side = [s for s in range(1, peak)]
        return side + [peak] + list(reversed(side))

    def get_sum(sums, start, end):
        return sums[end] - sums[start]

    def chisel(stones, p, start, end):
        cost = 0
        for i in range(start, end):
            stones_to_remove = stones[i] - p[i - start]
            if stones_to_remove < 0:
                return float('inf')
            cost += stones_to_remove
        return cost

    sums = [0]
    tot = 0
    for s in stones:
        tot += s
        sums.append(tot)

    l = len(stones)
    n = l if l % 2 else l - 1
    while n:
        p = construct_pyramid(n)
        res = float('inf')
        for i in range(l - n + 1):
            cost = get_sum(sums, 0, i) + chisel(stones, p, i, i + n) + get_sum(sums, i + n, l)
            res = min(res, cost)
        if res != float('inf'):
            return res
        n -= 2