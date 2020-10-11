# Does NOT work on negative integers
def bit_manip_if_else(x, y, b):
    bit_x = ''
    for i in range(len(bin(x)[2:])-1, -1, -1):
        bit_x += str((x >> i) & b)

    bit_y = ''
    for i in range(len(bin(y)[2:])-1, -1, -1):
        bit_y += str((y >> i) & (b ^ 1))

    return int(bit_x, 2) + int(bit_y, 2)

assert bit_manip_if_else(85,56,1) == 85
assert bit_manip_if_else(85,56,0) == 56

# DOES work on negative integers
def oper_if_else(x, y, b):
    return x * b + y * abs(b-1)

assert oper_if_else(-10,10,1) == -10
assert oper_if_else(-10,10,0) == 10