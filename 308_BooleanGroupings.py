def group_bools(bools):
    """Given a list of strings representing a Boolean expression BOOLS, returns the
    number of ways to group BOOLS using parentheses so that the entire expression
    evaluates to True.

    **Note: Assume that BOOLS is a valid Boolean expression. Also assume that there
    do not exist parentheses inside of BOOLS already.**

    >>> group_bools(['F', '|', 'T', '&', 'T'])
    3
    """
    assert bools, 'BOOLS cannot be an empty list.'

    inds = []
    for i,b in enumerate(bools):
        if b in 'TF':
            inds.append(i)
            if b == 'T':
                bools[i] = 'True'
            elif b == 'F':
                bools[i] = 'False'

    res = 0
    for i,s in enumerate(inds):
        for e in inds[i+1:]:
            bools.insert(e+1, ')')
            bools.insert(s, '(')

            if eval(''.join(bools)):
                res += 1
            else:
                break

            bools.remove('(')
            bools.remove(')')
    return res