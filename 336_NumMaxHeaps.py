# https://www.quora.com/How-many-Binary-heaps-can-be-made-from-N-distinct-elements

from math import factorial, floor, log2

def num_max_heaps(nums):
    """Given a list of numbers NUMS, computes the number of ways in which a max heap
    can be formed from NUMS.

    >>> num_max_heaps([1, 2, 3])
    2
    >>> num_max_heaps([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    3360
    """
    assert nums, 'NUMS cannot be an empty list.'

    def heap_recur(n):
        if n == 0:
            return 1
            
        h = int(floor(log2(n)))

        # num elements in left subtree of root up to second to last level
        p1 = 2**(h - 1) - 1
        # numb elements in last level
        p2 = n - 2**h + 1

        # num elements in left subtree of root
        l = p1 + min(p2, 2**(h - 1))
        # num elements in right subtree of root
        r = p1 + max(0, p2 - 2**(h - 1))

        return choose(n - 1, l) * heap_recur(l) * heap_recur(r)

    def choose(n, k):
        return factorial(n) // (factorial(k) * factorial(n - k))

    n = len(nums)
    if n == 0:
        return 0
    return heap_recur(n)