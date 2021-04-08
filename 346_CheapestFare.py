from heapq import heappush, heappop

def cheapest_fare(prices, a, b, k):
    """Given a list of tuples (source_city, destination, price) representing flights
    to and from two cities PRICES, strings of cities A and B, and positive integer K,
    determines the itinerary of flights i <= K from A to B that minimizes the price.

    >>> prices = [
    ...     ('JFK', 'ATL', 150),
    ...     ('ATL', 'SFO', 400),
    ...     ('ORD', 'LAX', 200),
    ...     ('LAX', 'DFW', 80),
    ...     ('JFK', 'HKG', 800),
    ...     ('ATL', 'ORD', 90),
    ...     ('JFK', 'LAX', 500)
    ... ]
    >>> cheapest_fare(prices, 'JFK', 'LAX', 3)
    (['JFK', 'ATL', 'ORD', 'LAX'], 440)
    >>> prices.remove(('ORD', 'LAX', 200))
    >>> prices.extend([('ORD', 'OAK', 100), ('OAK', 'LAX', 50)])
    >>> cheapest_fare(prices, 'JFK', 'LAX', 3)
    (['JFK', 'LAX'], 500)
    >>> cheapest_fare(prices, 'JFK', 'DFW', 1)
    ([], 0)
    """
    assert prices, 'PRICES cannot be an empty list.'
    assert a, 'A cannot be an empty string.'
    assert b, 'B cannot be an empty string.'
    assert k > 0, 'K must be a positive integer.'

    def dijkstra():
        price_to = {ap : float('inf') for ap in airports}
        dist_to = {ap : None for ap in airports}
        edge_to = {ap : None for ap in airports}
        price_to[a], dist_to[a] = 0, 0
        
        visited, q = set(), [(0, a)]    # (price, city) - price comes first bc of MinHeap
        while q:
            price, curr = heappop(q)
            visited.add(curr)
            for e,p in prices_dict.get(curr, []):
                if e in visited:
                    continue

                if price + p < price_to[e] and (dist_to[curr] <= k - 1 if e == b else True):
                    price_to[e] = price + p
                    dist_to[e] = dist_to[curr] + 1
                    edge_to[e] = curr
                heappush(q, (price_to[e], e))

        itinerary = []
        city = b
        while city:
            itinerary.insert(0, city)
            city = edge_to[city]
        return (itinerary, price_to[b]) if itinerary[0] == a and itinerary[-1] == b else ([], 0)

    prices_dict, airports = {}, set()
    for s,e,p in prices:
        prices_dict[s] = prices_dict.get(s, []) + [(e, p)]
        airports.add(s)
        airports.add(e)
    return dijkstra()