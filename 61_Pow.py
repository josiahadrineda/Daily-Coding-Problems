def pow(x, exp):
    if exp == 0:
        return 1
    elif exp < 0:
        return 1 / pow_helper(x, -exp)
    else:
        return pow_helper(x, exp)

def pow_helper(x, exp):
    mult = x

    i = 1
    while i*2 <= exp:
        mult *= mult
        i *= 2

    while i != exp:
        mult *= x
        i += 1

    return mult

assert pow(2, 0) == 1
assert pow(2, 5) == 32
assert pow(2, -5) == 1 / 32