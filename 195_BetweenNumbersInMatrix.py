def between_nums(matrix, i1, j1, i2, j2):
    """Given an N by M matrix of integers MATRIX and the row and column indices of numbers
    in the matrix I1, J1 and I2, J2, returns the count of numbers in MATRIX that are larger
    than MATRIX[I1][J1] and smaller than MATRIX[I2][J2] (the reverse may apply as well).

    *Note: Each row and column are sorted in increasing order.*

    >>> matrix = [
    ...     [1, 2, 3, 4, 5],
    ...     [2, 3, 4, 5, 6],
    ...     [3, 4, 5, 6, 7],
    ...     [4, 5, 6, 7, 8],
    ...     [5, 6, 7, 8, 9]
    ... ]
    >>> between_nums(matrix, 1, 1, 4, 4) # numbers between 3 and 9
    16
    >>> between_nums(matrix, 1, 1, 4, 4) # same deal, just flipped numbers
    16
    """
    assert matrix, 'MATRIX cannot be empty.'

    num1, num2 = matrix[i1][j1], matrix[i2][j2]
    if num1 > num2:
        small, large = num2, num1
    else:
        small, large = num1, num2
    
    cnt = 0
    for i in range(i1, i2 + 1):
        for j in range(len(matrix[0])):
            if small < matrix[i][j] < large:
                cnt += 1
    return cnt