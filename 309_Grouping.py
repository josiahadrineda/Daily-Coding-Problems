# https://www.geeksforgeeks.org/minimum-cost-to-remove-the-spaces-between-characters-of-a-string-by-rearranging-the-characters/

def min_cost(people):
    """Given a list of people sitting in a row of chairs PEOPLE, where PEOPLE[i] can
    either be a 1 (seat occupied) or a 0 (seat vacant), determine the minimum cost to
    make all people adjacent to each other.

    >>> min_cost([0, 1, 1, 0, 1, 0, 0, 0, 1])
    5
    """
    assert people, 'PEOPLE cannot be an empty list.'

    n = people.count(1)

    if n == 1:
        return 0

    res, ppl, sts = 0, 0, 0
    for p in people:
        if p:
            if sts:
                res += min(n - ppl, ppl) * sts
                sts = 0
            ppl += 1
        else:
            sts += 1
    return res