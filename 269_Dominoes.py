def dominoes(doms):
    """Given a string of domino positions DOMS (L = pushed left, R = pushed right,
    . = standing upright), determines the position of DOMS after the pushes.

    >>> dominoes('.L.R....L')
    'LL.RRRLLL'
    >>> dominoes('..R...L.L')
    '..RR.LLLL'
    """
    assert doms, 'DOMS cannot be an empty string.'

    n = len(doms)
    doms_list = list(doms)
    next_state = []
    while True:
        for i, dom in enumerate(doms_list):
            if dom in 'LR':
                next_state.append(dom)
            else:
                l, r = False, False
                if i + 1 < n and doms_list[i + 1] == 'L':
                    l = True
                if i - 1 > 0 and doms_list[i - 1] == 'R':
                    r = True

                if l and not r:
                    next_state.append('L')
                elif not l and r:
                    next_state.append('R')
                else:
                    next_state.append('.')

        if doms_list == next_state:
            return ''.join(doms_list)
        doms_list, next_state = list(next_state), []