def integer_palindrome(n):
    """Given a positive integer N, returns whether or not N is a palindrome.

    **Note: Conversion from int to str is NOT allowed.**

    >>> integer_palindrome(121)
    True
    >>> integer_palindrome(888)
    True
    >>> integer_palindrome(678)
    False
    """
    assert n > 0, 'N must be a positive integer.'

    digits = []
    while n:
        last, n = n % 10, n // 10
        digits.append(last)

    for i in range(len(digits) // 2):
        if digits[i] != digits[~i]:
            return False
    return True