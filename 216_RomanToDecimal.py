romans = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def roman_to_decimal(s):
    """Given a string in Roman numeral format S, converts S to decimal.

    >>> roman_to_decimal('I')
    1
    >>> roman_to_decimal('IV')
    4
    >>> roman_to_decimal('XL')
    40
    >>> roman_to_decimal('XIV')
    14
    """
    assert s, 'S cannot be an empty string.'

    prev, s = s[-1], s[:-1][::-1]
    res = romans[prev]
    for char in s:
        res += romans[char] * (-1 if romans[char] < romans[prev] else 1)
        prev = char
    return res