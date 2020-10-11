from math import sqrt

def square_int_sum(n):
    """Given a positive integer N, finds the smallest number
    of squared integers which summ to N.

    >>> square_int_sum(13)
    2
    >>> square_int_sum(25)
    1
    >>> square_int_sum(27)
    3
    """
    assert n > 0, 'N must be a positive integer.'

    squares = [1]
    i = 2
    while i**2 <= n:
        squares.insert(0, i**2)
        i += 1

    return square_int_sum_bfs(squares, n)

# Because of the nature of queues, we are allowed to return instead of traversing
# all other possibilities. By the time we get to the return statement, a global
# solution has already been reached.
def square_int_sum_bfs(squares, n):
    q = [(n, 0)]
    while q:
        n, curr = q.pop(0)
        for s in squares:
            diff = n - s
            if diff == 0:
                return curr + 1
            elif diff > 0:
                q.append((diff, curr+1))