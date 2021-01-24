from functools import lru_cache

def throw_dice(n, faces, total):
    """Given positive integers N, FACES, and TOTAL, determines the number of ways to
    reach TOTAL by rolling N dice with FACES faces each.

    >>> throw_dice(2, 6, 1)
    0
    >>> throw_dice(3, 6, 7)
    15
    >>> throw_dice(100, 20, 200)
    45272586364201938530001766805903602010840963682813036906765
    """
    assert n > 0 and faces > 0 and total > 0, 'N, FACES, and TOTAL must be positive integers.'

    @lru_cache(maxsize=None)
    def throw_dice_recur(n, faces, total):
        if n == 1:
            if total <= 0:
                return 0
            return faces >= total
        else:
            res = 0
            for face in range(1, faces + 1):
                res += throw_dice_recur(n - 1, faces, total - face)
            return res
    return throw_dice_recur(n, faces, total)