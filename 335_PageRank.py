from heapq import heappush, heappop

def page_rank(websites, d=0.85):
    """Suppose there are N sites, and each site i has a certain count Ci of outgoing
    links. Given a directed graph of links between varioius websites, calculates
    each website's page rank.

    >>> websites = {
    ...     'a': [('b', 1), ('c', 1)],
    ...     'b': [('c', 1)],
    ...     'c': []
    ... }
    >>> scores = page_rank(websites)
    >>> rank(scores)
    ['c', 'b', 'a']
    >>> websites = {
    ...     'google.com': [('facebook.com', 2587), ('reddit.com', 420), ('youtube.com', 5012)],
    ...     'khanacademy.org' : [('google.com', 3359)],
    ...     'stackoverflow.com': [('google.com', 1234)],
    ...     'coolmathgames.com': [('facebook.com', 42), ('reddit.com', 696), ('youtube.com', 4001)],
    ...     'facebook.com': [('youtube.com', 4321)],
    ...     'reddit.com': [],
    ...     'youtube.com': []
    ... }
    >>> scores = page_rank(websites)
    >>> rank(scores)
    ['google.com', 'youtube.com', 'facebook.com', 'reddit.com', 'coolmathgames.com', 'khanacademy.org', 'stackoverflow.com']
    """
    assert websites, 'WEBSITES cannot be an empty graph.'

    def has_cycle():
        def has_cycle_recur(w):
            if w in visited:
                return False

            visited.add(w)
            for neighbor, _ in websites[w]:
                if has_cycle_recur(neighbor):
                    return True
            return False

        visited = set()
        return has_cycle_recur(website_names[0])

    def calculate_score(w):
        if w in scores:
            return scores[w]

        tot = 0
        for neighbor in ins[w]:
            tot += calculate_score(neighbor) / outs[neighbor]
        scores[w] = ((1 - d) / n) + (d * tot)
        return scores[w]

    website_names = sorted(list(websites.keys()))
    n = len(website_names)

    if has_cycle():
        return {w : -1.0 for w in website_names}

    ins = {}
    outs = {}
    for w in website_names:
        ins[w] = ins.get(w, [])
        tot = 0
        for o,c in websites[w]:
            ins[o] = ins.get(o, []) + [w]
            tot += c
        outs[w] = tot

    scores = {}
    for w in website_names:
        calculate_score(w)
    return [(w, scores[w]) for w in website_names]

def rank(scores):
    h = []
    for w,s in scores:
        heappush(h, (-s, w))

    ranked_websites = []
    while h:
        s,w = heappop(h)
        ranked_websites.append(w)
    return ranked_websites