def add_subtract(x):
    """A function that alternately adds and subtracts curried integers.

    >>> temp = add_subtract(7)
    7
    >>> temp = add_subtract(1)(2)(3)
    1
    3
    0
    >>> temp = add_subtract(-5)(10)(3)(9)
    -5
    5
    2
    11
    """

    def add_sub_helper(tot, k):
        def helper(y):
            if k % 2 == 0:
                return add_sub_helper(tot + y, k + 1)
            return add_sub_helper(tot - y, k + 1)

        print(tot)
        return helper

    return add_sub_helper(x, 0)

def add_subtract_k(k):
    """Like add_subtract except only returning a result after exactly K arguments.

    >>> add_subtract_k(1)(7)
    7
    >>> add_subtract_k(3)(1)(2)(3)
    0
    >>> add_subtract_k(4)(-5)(10)(3)(9)
    11
    """
    assert k > 0, 'K must be a positive integer.'

    def add_sub_k_helper(tot, k):
        def helper(x):
            if K - k == 0 or (K - k) % 2 == 1:
                return add_sub_k_helper(tot + x, k - 1)
            return add_sub_k_helper(tot - x, k - 1)
        
        if k == 0:
            return tot
        return helper

    K = k
    return add_sub_k_helper(0, k)

def add_subtract_k_clever(k):
    """Like add_subtract_k but all accomplished with one line.

    >>> add_subtract_k_clever(1)(7)
    7
    >>> add_subtract_k_clever(3)(1)(2)(3)
    0
    >>> add_subtract_k_clever(4)(-5)(10)(3)(9)
    11
    """
    
    return (lambda f, tot, n: tot if n == 0 else lambda x: f(f, tot + x, n - 1) if k - n == 0 or (k - n) % 2 == 1 else f(f, tot - x, n - 1))(lambda f, tot, n: tot if n == 0 else lambda x: f(f, tot + x, n - 1) if k - n == 0 or (k - n) % 2 == 1 else f(f, tot - x, n - 1), 0, k)