from functools import lru_cache

def jump_game(steps):
    """Given a list of nonnegative integers STEPS, where STEPS[i] represents
    the maximum number of steps one can move forward, returns the minimum
    number of steps to reach the end of STEPS (assume the starting position
    is at index 0 and it is possible to reach the end of STEPS).

    >>> jump_game([6, 2, 4, 0, 5, 1, 1, 4, 2, 9])
    2
    """
    assert steps, 'STEPS cannot be an empty list.'

    @lru_cache(maxsize=None)
    def dfs(s, e):
        if s == e:
            return 0
        else:
            res = float('inf')
            if is_valid(s):
                for step in range(steps[s], 0, -1):
                    res = min(res, dfs(s + step, e))
            return 1 + res

    def is_valid(s):
        return s < len(steps) and steps[s] != 0

    return dfs(0, len(steps) - 1)