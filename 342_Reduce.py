def manual_reduce(lst, func, start):
    """A manual implementation of the reduce function - a function that aggregates the objects in LST
    via taking the START value, applying FUNC to START and LST[0], and repeating the process for the
    resultant value and LST[1] ... LST[len(LST) - 1].

    >>> from operator import add, mul
    >>> manual_reduce(['he', 'llo ', 'wor', 'ld!'], add, '')
    'hello world!'
    >>> manual_reduce([1, 2, 3, 4], add, 0)
    10
    >>> manual_reduce([1, 2, 3, 4], mul, 1)
    24
    """
    
    if not lst:
        return start
    return manual_reduce(lst[1:], func, func(start, lst[0]))