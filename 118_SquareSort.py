def square_sort(nums):
    """
    Given a list of integers, quare the elements
    and give the output in sorted order.

    >>> square_sort([])
    []
    >>> square_sort([0])
    [0]
    >>> square_sort([-1, 1])
    [1, 1]
    >>> square_sort([0, 2, 3])
    [0, 4, 9]
    >>> square_sort([-9, -2, 0])
    [0, 4, 81]
    >>> square_sort([-9, -2, 0, 2, 3])
    [0, 4, 4, 9, 81]
    """
    
    return list(map(lambda x: x*x, sorted(list(map(abs, nums)))))