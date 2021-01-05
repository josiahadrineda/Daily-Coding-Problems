def zigzag_print(s, k):
    """Given a string S and a positive integer K,
    prints S in zigzag form with width K.

    >>> zigzag_print('thisisazigzag', 4)
    t     a     g
     h   s z   a 
      i i   i z  
       s     g   
    >>> zigzag_print('hello', 10)
    h    
     e   
      l  
       l 
        o
    >>> zigzag_print('foobar', 2)
    f o a 
     o b r
    >>> zigzag_print('apple', 1)
    apple
    """
    assert s, 'S cannot be an empty string.'
    assert k > 0, 'K must be a positive integer'

    if k == 1:
        print(s)
        return

    rows = [[] for _ in range(k)]
    i, dir = 0, 1
    for c in s:
        rows[i].append(c)
        for j in range(len(rows)):
            if j != i:
                rows[j].append(' ')

        if dir == 1 and i == k - 1:
            dir = -1
        elif dir == -1 and i == 0:
            dir = 1
        i += dir

    i = 1
    while i < len(rows):
        if rows[i].count(' ') == len(rows[i]):
            rows.pop(i)
        else:
            i += 1

    for r in rows:
        print(''.join(r))
    return