from functools import reduce

def two_unique_elements(arr):
    """Given an array of intergers in which two integers appear
    exactly once and all other elements appear exactly twice,
    finds the two elements that appear only once.

    >>> two_unique_elements([2, 4, 6, 8, 10, 2, 6, 10])
    [4, 8]
    """
    assert arr, 'Cannot find unique elements in empty array.'

    x = lambda a, b: a ^ b
        
    xor = reduce(x, arr)
    rsb = xor & ~(xor-1)
    l1, l2 = [], []
    for el in arr:
        if rsb & el:
            l1.append(el)
        else:
            l2.append(el)
    
    n1 = reduce(x, l1)
    n2 = reduce(x, l2)
    return [n1, n2]