def alphabetical_column_id(n):
    """Spreadsheets often use this alphabetical encoding for its columns:
    'A', 'B', 'C', ..., 'AA', 'AB', ..., 'ZZ', 'AAA', 'AAB', ....

    Given a positive integer N representing column number, returns its
    alphabetical column ID.

    >>> alphabetical_column_id(1)
    'A'
    >>> alphabetical_column_id(27)
    'AA'
    >>> alphabetical_column_id(52)
    'AZ'
    """
    assert n > 0, 'N must be a positive integer.'

    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    k = len(alpha)
    id = []

    while n:
        letter = alpha[(n-1) % k]
        id.append(letter)
        n = (n-1) // k
    return ''.join(reversed(id))