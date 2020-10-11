def sqrt(n):
    """Finds (or approximates) the square root of N.
    
    >>> sqrt(9)
    3.0
    >>> sqrt(2)
    1.414213562373095
    >>> sqrt(-1)
    0.0
    """
    
    def f(x):
        return x*x - n

    def df(x):
        return 2*x

    if n <= 0:
        return 0.0
    return newtons_method(f, df)

def newtons_method(f, df, guess=1, attempts=1000000):
    """Uses Newton's Method to approximate the positive zero of a differentiable function.
    """

    def accurate(x, err=1e-15):
        return abs(f(x)) <= err

    def approximate(guess):
        return guess - f(guess) / df(guess)

    i = 0
    while i < attempts or not accurate(guess):
        guess = approximate(guess)
        i += 1
    return guess 