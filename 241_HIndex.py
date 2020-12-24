def h_index(citations):
    """In academia, the h-index is a metric used to calculate the impact of a researcher's
    papers. It is calculated as follows:

    A researcher has index h if at least h of her N paperes have h citations each. If there
    are multiple h satisfying this formula, the maximum is chosen.

    Given a list of citations for N papers CITATIONS, calculates the researcher's h-index.

    >>> h_index([4, 3, 0, 1, 5])
    3
    """
    assert citations, 'CITATIONS cannot be an empty list.'

    citations.sort(reverse=True)

    res = 0
    for i in range(len(citations)):
        res = max(res, min(i + 1, citations[i]))
    return res