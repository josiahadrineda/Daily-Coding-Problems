# https://en.wikipedia.org/wiki/Nim#Mathematical_theory

def nim(heaps):
    """The game of Nim is played as follows: Starting with 3 heaps of varying size,
    two players take turns removing one of more items from a single heap. The player
    who eventually is forced to take the last item loses. Given 3 heap sizes HEAPS,
    determines whether the first player has a forced win.

    >>> nim([3, 4, 5])
    True
    """
    assert len(heaps) == 3 and all([h > 0 for h in heaps]), 'HEAPS must be a list with 3 positive values.'

    nim_sum = heaps[0]
    for h in heaps[1:]:
        nim_sum ^= h

    for h in heaps:
        if nim_sum ^ h < h:
            return True
    return False