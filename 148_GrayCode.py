def gray_code(n):
    """Given a nonnegative integer of bits N, generates a possible gray code for it.

    >>> gray_code(1)
    ['0', '1', '1', '0']
    >>> gray_code(2)
    ['00', '01', '11', '10']
    >>> gray_code(3)
    ['000', '001', '011', '010', '110', '111', '101', '100']
    """
    assert n > 0, 'N must be a nonnegative integer.'

    if n <= 2:
        code = [''] * 2**2
    else:
        code = [''] * 2**n

    for i in range(1, n+1):
        bit = '0'
        switch = 2**(i-1)
        reverse = False
        for j in range(len(code)):
            if j != 0 and j % switch == 0:
                if reverse:
                    bit = str(1 - int(bit))
                bit = str(1 - int(bit))
                reverse = not reverse
            code[j] = push_digit(code[j], bit)
    return code

def push_digit(num, digit):
    return digit + num