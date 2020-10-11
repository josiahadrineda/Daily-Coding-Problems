def divide(a, b):
    res = 0
    while a >= b:
        a, res = a - b, res + 1
    return res

assert divide(1,1) == 1
assert divide(5,3) == 1
assert divide(6,3) == 2
assert divide(24,7) == 3
assert divide(24,8) == 3