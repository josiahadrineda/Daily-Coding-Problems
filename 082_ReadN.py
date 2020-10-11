def read7(s):
    if len(s) <= 7:
        seg, s = s, ''
    else:
        seg, s = s[:7], s[7:]
    return seg, s

def readN(s, n):
    res = ''
    while len(res) < n and s != '':
        seg, s = read7(s)
        res += seg

    diff = abs(len(res) - n)
    if len(res) + len(s) < diff:
        pass
    elif len(res) < n:
        for _ in range(diff):
            res, s = res + s[:1], s[1:]
    elif len(res) > n:
        for _ in range(diff):
            s, res = res[-1] + s, res[:-1]
    return res, s

s = 'Hello World'
res, s = readN(s, 6)
assert res == 'Hello '
res, s = readN(s, 5)
assert res == 'World'

s = 'Hello World'
res, s = readN(s, 11)
assert res == 'Hello World'

s = 'Hello World'
res, s = readN(s, 50)
assert res == 'Hello World'