from heapq import heappush, heappop

# TC: O(S log K), SC: O(K)
def smallest_string(s, k):
    """Given a string S and a nonnegative integer K, determines the smallest string
    that can be created by removing and appending one of the first K characters of S
    (this can be done an unlimited number of times).

    >>> smallest_string('daily', 1)
    'ailyd'
    >>> smallest_string('daily', 2)
    'adily'
    >>> smallest_string('bbcbb', 2)
    'bbbbc'
    >>> smallest_string('gaurang', 3)
    'agangru'
    """
    assert s, 'S cannot be an empty string.'
    assert k >= 0, 'K must be a nonnegative integer.'
    assert k <= len(s), 'K cannot be greater than the length of S.'

    n = len(s)

    # Special case: k = 0
    # TC: O(1), SC: O(1)
    if k == 0:
        return s

    # Special case: k = 1
    # TC: O(SK), SC: O(1)
    if k == 1:
        res, temp = s, s + s
        for i in range(k + 1):
            res = min(res, temp[i:n+i])
        return res

    # Other cases: k > 1
    # TC and SC specified above
    q, temp = [], s
    for _ in range(k):
        heappush(q, temp[0])
        temp = temp[1:]
    
    res = ''
    while q:
        res += heappop(q)
        if temp:
            heappush(q, temp[0])
            temp = temp[1:]
    return res