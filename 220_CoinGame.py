def coin_game(coins, max_score=0, max_player=True):
    """Given a row of coins COINS, where coins[i] = the value of the coin at
    the ith position, returns the maximum possible score one can achieve while
    playing the "coin game", assuming the other player plays optimally. The
    coin game is a two-player game where each player takes a coin either from
    the start of the row or the end of the row, ending when all coins are taken.
    The player with the highest aggregated value of coins is the winner.

    >>> coin_game([1, 2, 3, 4, 5])
    9
    >>> coin_game([1, 1, 5, 1, 5, 10, 25, 50, 50, 10, 10, 5, 1, 5, 5, 100, 1])
    198
    """

    if not coins:
        return max_score

    if max_player:
        take_first = coin_game(coins[1:], max_score + coins[0], False)
        take_last = coin_game(coins[:-1], max_score + coins[-1], False)
        return max(take_first, take_last)
    else:
        first, last = coins[0], coins[-1]
        if first > last:
            return coin_game(coins[1:], max_score, True)
        else:
            return coin_game(coins[:-1], max_score, True)