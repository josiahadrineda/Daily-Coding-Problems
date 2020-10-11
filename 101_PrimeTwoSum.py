def primes_below_n(n):
    """
    Returns a list of all prime integers within the interval [2, n).

    >>> primes_below_n(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    """
    assert n > 2, 'n must be greater than 2.'

    def list_comp(filter_func, n, lb):
        return [x for x in range(lb, n) if filter_func(x)]

    def is_prime(n):
        return len(list_comp(lambda x: n % x == 0, n, 1)) == 1

    return list_comp(is_prime, n, 2)

def prime_two_sum(n):
    """
    Return two primes whose sum is n.
    *n must be an even integer greater than 2*

    >>> prime_two_sum(4)
    '2 + 2 = 4'

    >>> prime_two_sum(12)
    '5 + 7 = 12'

    >>> prime_two_sum(50)
    '3 + 47 = 50'
    """
    assert n % 2 == 0, 'n must be an even integer.'
    assert n > 2, 'n must be greater than 2.'

    primes = primes_below_n(n)
    for p1 in primes:
        for p2 in primes:
            if p1 + p2 == n:
                return f'{p1} + {p2} = {n}'