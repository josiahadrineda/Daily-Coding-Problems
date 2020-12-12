from functools import lru_cache

def snakes_and_ladders(snakes, ladders):
    """Given two dictionaries representing the tiles in which snakes and ladders
    reside, SNAKES and LADDERS, computes the minimum number of turns needed to
    beat the game.

    >>> snakes = {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
    >>> ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
    >>> snakes_and_ladders(snakes, ladders)
    7
    """

    @lru_cache(maxsize=None)
    def optimal_game(moves, start=1, goal=100):
        nonlocal min_moves
        if moves >= min_moves or start > goal:
            return
        elif start == goal:
            min_moves = min(min_moves, moves)
        else:
            for i in range(6, 0, -1):
                start += i
                if snakes.get(start):
                    optimal_game(moves + 1, snakes[start], goal)
                elif ladders.get(start):
                    optimal_game(moves + 1, ladders[start], goal)
                else:
                    optimal_game(moves + 1, start, goal)
                start -= i
    
    min_moves = float('inf')
    optimal_game(0)
    return min_moves