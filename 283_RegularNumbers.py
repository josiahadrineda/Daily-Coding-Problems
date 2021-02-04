def regular_numbers(n):
    """Given a positive integer N, returns the first N regular numbers, where a
    regular number is defined as a number whose only prime divisors are 2, 3, and 5.

    >>> regular_numbers(15)
    [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24]
    """
    assert n > 0, 'N must be a positive integer.'

    def is_prime(n):
        for i in range(2, n):
            if not n % i:
                return False
        return True

    primes, reg = [], []
    i = 1
    while len(reg) < n:
        if i < 7:
            reg.append(i)
        elif is_prime(i):
            primes.append(i)
        elif all([i % p for p in primes]):
            reg.append(i)
        i += 1
    return reg