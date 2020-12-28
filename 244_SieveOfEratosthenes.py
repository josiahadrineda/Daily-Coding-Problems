def sieve(n):
    """Returns all prime numbers less than positive integer N greater than 1.

    >>> sieve(50)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """
    assert n > 1, 'N must be a positive integer greater than 1.'

    if n == 2:
        return []

    nums = [x for x in range(2, n)]
    i = 2
    while i <= n**(1/2):
        num = i * 2
        while num < n:
            if num in nums:
                nums.remove(num)
            num += i
        i += 1
    return nums

def prime_gen():
    """Lazily computes prime numbers.

    >>> gen = prime_gen()
    >>> list([next(gen) for _ in range(15)])
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """

    primes = [2]
    i = 3
    while True:
        yield primes[-1]
        while not all([i % x for x in primes]):
            i += 1
        primes.append(i)