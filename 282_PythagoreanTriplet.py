def pythagorean_triplet(a, b, c):
    """Given three positive integers A, B, and C, determines whether or not a
    Pythagorean triplet exists among them.

    **Note: A Pythagorean triplet satisfies the equation x^2 + y^2 = z^2.**

    >>> pythagorean_triplet(5, 4, 3)
    True
    >>> pythagorean_triplet(12, 5, 13)
    True
    >>> pythagorean_triplet(1, 2, 3)
    False
    """
    assert a > 0, 'A must be a positive integer.'
    assert b > 0, 'B must be a positive integer.'
    assert c > 0, 'C must be a positive integer.'

    nums = [a, b, c]
    PERMUTATIONS = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
    
    for p in PERMUTATIONS:
        i, j, k = p
        if nums[i]**2 + nums[j]**2 == nums[k]**2:
            return True
    return False