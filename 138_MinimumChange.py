def min_change(n):
    """Using standard US coin denominations (1c, 5c, 10c, 25c),
    finds the minimum number of coins required to make N cents.

    >>> min_change(0)
    0
    >>> min_change(4)
    4
    >>> min_change(5)
    1
    >>> min_change(16)
    3
    """
    assert n >= 0, 'Cannot find negative change value.'
    
    coins = [25, 10, 5, 1]
    i, res = 0, 0
    while n:
        change = n // coins[i]
        res, n = res + change, n - change * coins[i]
        i += 1
    return res