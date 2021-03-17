def mice_to_holes(mice, holes):
    """Given the locations of N mice MICE and N holes HOLES (on a number line), returns
    the largest distance a mouse has to cover to reach a hole, where there must exist a
    1-to-1 mapping from MICE to HOLES.

    >>> mice_to_holes([1, 4, 9, 15], [10, -5, 0, 16])
    6
    """
    assert mice, 'MICE cannot be an empty list.'
    assert holes, 'HOLES cannot be an empty list.'

    mice.sort()
    holes.sort()

    return max(abs(m - h) for m,h in zip(mice, holes))