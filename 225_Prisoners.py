def prisoners(n, k):
    """Given two positive integers N and K, where N represents the number of prisoners to be executed
    and K represents the order of succession with regards to execution, returns the last prisoner
    to be executed.

    >>> prisoners(5, 2) # The order of execution is [2, 4, 1, 5, 3]
    3
    >>> prisoners(12, 4) # The order of execution is a pain to write out...
    1
    """
    assert n > 0, 'N must be a positive integer.'
    assert k > 0, 'K must be a positive integer.'

    prisoners = [i for i in range(1, n + 1)]
    start = k % n - 1
    while len(prisoners) > 1:
        prisoners.pop(start)
        start = (start + (k - 1)) % len(prisoners)
    return prisoners[0]