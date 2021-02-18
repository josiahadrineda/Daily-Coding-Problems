def drinks(likes):
    """Given a dictionary mapping customers to their favorite drinkes LIKES, returns
    the minimum number of drinks needed to satisfy all customers.

    >>> likes = {
    ...     0: [0, 1, 3, 6],
    ...     1: [1, 4, 7],
    ...     2: [2, 4, 7, 5],
    ...     3: [3, 2, 5],
    ...     4: [5, 8]
    ... }
    >>> drinks(likes)
    2
    """
    assert likes, 'LIKES cannot be an empty dictionary.'

    def drinks_recur(rem_drinks, drinks, cust):
        if not cust:
            return rem_drinks

        res = drinks
        for drink in drinks:
            cand = drinks_recur(
                rem_drinks | {drink},
                drinks - {drink},
                cust - drinks_to_cust[drink]
            )
            if len(cand) < len(res):
                res = cand
        return res

    drinks_to_cust = {}
    for cust, drinks in likes.items():
        for drink in drinks:
            if drinks_to_cust.get(drink) == None:
                drinks_to_cust[drink] = set()
            drinks_to_cust[drink].add(cust)

    return len(
        drinks_recur(
            set(),
            set(drinks_to_cust.keys()),
            set(likes.keys())
        )
    )