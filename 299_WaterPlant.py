def min_cost(pipes):
    """Given a dictionary representation of a directed graph PIPES, where keys are
    either the plant itself or a neighboring house and values are pipes associated
    with a cost connecting a house/plant to another house/plant, returns the minimum
    cost required to connect all houses to the plant.

    >>> pipes = {
    ...     'plant': {'A': 1, 'B': 5, 'C': 20},
    ...     'A': {'C': 15},
    ...     'B': {'C': 10},
    ...     'C': {}
    ... }
    >>> min_cost(pipes)
    16
    """
    assert pipes, 'PIPES cannot be an empty dictionary.'

    houses = set(pipes) - {'plant'}
    costs = {}
    for house in houses:
        costs[house] = float('inf')
    
    q = ['plant']
    while q:
        curr = q.pop(0)
        for house, cost in pipes[curr].items():
            q.append(house)
            costs[house] = min(costs[house], cost)
    return sum(costs.values())