# https://www.geeksforgeeks.org/the-celebrity-problem/

def celebrity(n, _connections):
    """At a party, there is a single person who everyone knows, but who does not know
    anyone in return (the "celebrity"). To help figure out who this is, you have access
    to an O(1) method called knows(a, b), which returns True if person A knows person B,
    else False.

    Given a positive integer N representing the # of people at the party as well as the
    above operation, identifies the celebrity in O(N) time.

    **Note: _CONNECTIONS is NOT meant to be accessible. It is only meant for knows(a, b).
    Also assume that a celebrity always exists.**

    >>> _connections = {
    ...     0: set([1, 2, 3, 4]),
    ...     1: set([2]),
    ...     2: set([]),
    ...     3: set([0, 2, 4]),
    ...     4: set([2, 3])
    ... }
    >>> celebrity(5, _connections)
    2
    """
    assert n > 0, 'N must be a positive integer.'
    assert _connections, '_CONNECTIONS cannot be an empty dictionary.'

    def knows(a, b):
        return b in _connections[a]

    def celeb_recur(n):
        if not n:
            return 0

        a = celeb_recur(n - 1)
        b = n - 1
        if knows(a, b):
            return b
        return a
    return celeb_recur(n)