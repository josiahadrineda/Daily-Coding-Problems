def majority_element(lst):
    """Given a list of elements LST, finds the majority element,
    aka the element that appears more than half the time. Assume
    that such an element exists.

    *> len(lst) // 2*

    >>> majority_element([2, 2, 3])
    2
    >>> majority_element([1, 2, 1, 1, 3, 4, 1])
    1
    >>> majority_element([3, 4, 3, 5, 3, 6, 3, 7, 3, 8, 3, 9, 3])
    3
    """
    assert lst and len(lst) > 0, 'Cannot find majority element of empty list.'

    candidate, freq = None, 0
    for el in lst:
        if not candidate:
            candidate, freq = el, 1
        elif el != candidate:
            freq -= 1
        else:
            freq += 1

        if freq < 0:
            candidate, freq = el, 1
    return candidate
