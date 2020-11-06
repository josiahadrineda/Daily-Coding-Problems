def stock_with_transaction_fee(prices, fee):
    """Given an list of nonnegative integers PRICES, for which the i-th
    element is the price of a given stock on day i, as well as a nonnegative
    integer FEE representing a transaction fee, calculates the maximum profit.

    >>> stock_with_transaction_fee([1, 3, 2, 8, 4, 10], 2)
    9
    """
    assert prices, 'PRICES cannot be an empty list.'
    assert fee >= 0, 'FEE must be a nonnegative integer.'

    sold, bought = 0, float('-inf')
    for price in prices:
        sold, bought = max(sold, bought + price), max(bought, sold - price - fee)
    return sold