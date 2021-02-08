from heapq import heappush

def k_most_similar_websites(traffic, k):
    """Given a list of tuples (website, users) representing the flow of users TRAFFIC
    as well as a positive integer K, identifies the top K pairs of websites with the
    greatest similarity.

    >>> traffic = [
    ...     ('a', 1), ('a', 3), ('a', 5),
    ...     ('b', 2), ('b', 6),
    ...     ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5),
    ...     ('d', 4), ('d', 5), ('d', 6), ('d', 7),
    ...     ('e', 1), ('e', 3), ('e', 5), ('e', 6)
    ... ]
    >>> k_most_similar_websites(traffic, 3)
    [('a', 'e'), ('a', 'c'), ('b', 'd')]
    """
    assert traffic, 'TRAFFIC cannot be an empty list.'
    assert k > 0, 'K must be a positive integer.'

    # Higher score = More similarity
    def sim_score(web_a, web_b):
        intersection = web_a & web_b
        union = web_a | web_b
        return len(intersection) / len(union)

    traffic_dict = {}
    for web, users in traffic:
        if traffic_dict.get(web) == None:
            traffic_dict[web] = set()
        traffic_dict[web].add(users)
    webs = sorted(list(traffic_dict))

    heap = []
    for i, a in enumerate(webs):
        for b in webs[i+1:]:
            web_a, web_b = traffic_dict[a], traffic_dict[b]
            ss = sim_score(web_a, web_b)
            heappush(heap, (-ss, (a, b)))
    return [pair for ss, pair in heap[:k]]