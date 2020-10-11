# Key takeaway: WATCH ALGO EXPERT !!!
# https://www.youtube.com/watch?v=Pw6lrYANjz4

# TC: O(n^2 * k)
# SC: O(nk)
def max_profit_1(prices, k):
    """
    Given an array of numbers representing the stock prices
    of a company in chronological order and an integer k,
    returns the maximum profit you can make from k transactions.

    >>> max_profit_1([5,2,4,0,1], 1)
    2
    >>> max_profit_1([5,2,4,0,1], 2)
    3
    """
    assert prices, 'No prices listed.'
    for price in prices: assert price >= 0, 'Price cannot be negative.'
    assert k >= 0, 'Cannot make negative transactions.'

    if k == 0:
        return 0

    profits = [[0 for p in prices] for t in range(k + 1)]
    for t in range(1, k + 1):
        for p in range(1, len(prices)):
            max_prev = float('-inf')
            for p2 in range(p):
                max_prev = max(max_prev, profits[t - 1][p2] - prices[p2])
            profits[t][p] = max(profits[t][p - 1], max_prev + prices[p])
    return profits[-1][-1]

# TC: O(nk)
# SC: O(nk)
def max_profit_2(prices, k):
    """
    Given an array of numbers representing the stock prices
    of a company in chronological order and an integer k,
    returns the maximum profit you can make from k transactions.

    >>> max_profit_2([5,2,4,0,1], 1)
    2
    >>> max_profit_2([5,2,4,0,1], 2)
    3
    """
    assert prices, 'No prices listed.'
    for price in prices: assert price >= 0, 'Price cannot be negative.'
    assert k >= 0, 'Cannot make negative transactions.'

    if k == 0:
        return 0

    profits = [[0 for p in prices] for t in range(k + 1)]
    for t in range(1, k + 1):
        max_thus_far = float('-inf')
        for p in range(1, len(prices)):
            max_thus_far = max(max_thus_far, profits[t - 1][p - 1] - prices[p - 1])
            profits[t][p] = max(profits[t][p - 1], max_thus_far + prices[p])
    return profits[-1][-1]

# TC: O(nk)
# SC: O(n)
def max_profit_3(prices, k):
    """
    Given an array of numbers representing the stock prices
    of a company in chronological order and an integer k,
    returns the maximum profit you can make from k transactions.

    >>> max_profit_3([5,2,4,0,1], 1)
    2
    >>> max_profit_3([5,2,4,0,1], 2)
    3
    """
    assert prices, 'No prices listed.'
    for price in prices: assert price >= 0, 'Price cannot be negative.'
    assert k >= 0, 'Cannot make negative transactions.'

    if k == 0:
        return 0

    evens = [0 for p in prices]
    odds = [0 for p in prices]
    for t in range(1, k + 1):
        max_thus_far = float('-inf')
        if t % 2 == 1:
            curr = odds
            prev = evens
        else:
            curr = evens
            prev = odds
        for p in range(1, len(prices)):
            max_thus_far = max(max_thus_far, prev[p - 1] - prices[p - 1])
            curr[p] = max(curr[p - 1], max_thus_far + prices[p])
    return curr[-1]