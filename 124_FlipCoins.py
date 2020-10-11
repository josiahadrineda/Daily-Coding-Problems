from math import ceil, log

def flip_coins(n):
    """
    You have n fair coins and you flip them all at the same time.
    Any that come up tails you set aside. The ones that come up
    heads you flip again. Returns the number of rounds do you
    expect to play before only one coin remains.

    >>> flip_coins(1)
    0
    >>> flip_coins(2)
    1
    >>> flip_coins(100)
    7
    >>> flip_coins(200)
    8
    """
    assert n > 0, 'Cannot flip zero or negative coins.'

    # As the probability for a coin flip is 0.5,
    # The number of coins is expected to decrease by 0.5,
    # After each subsequent round.
    return ceil(log(n, 2))