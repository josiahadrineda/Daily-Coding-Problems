from functools import lru_cache

@lru_cache(maxsize=None)
def collatz(n):
    """Given a positive integer N, computes the length of the Collatz sequence
    starting at N (excluding 1).
    
    A Collatz sequence can be defined as follows:
    1. If N is even, the next number in the sequence is N / 2
    2. Otherwise, the next number in the sequence is 3N + 1

    The conjecture states that every such sequence eventually reaches the number 1.

    >>> collatz(5)
    5
    >>> collatz(50)
    24
    """
    assert n > 0, 'N must be a positive integer.'

    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + collatz(n // 2)
    return 1 + collatz(3*n + 1)

# What input N <= 1000000 gives the longest sequence?
global_max = float('-inf')
for i in range(2, 1000001):
    global_max = max(global_max, collatz(i))
    
print(global_max)
# Result: 524