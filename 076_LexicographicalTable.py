def lexicographical_table(table):
    res = 0
    if not table or len(table) <= 1:
        return res

    for j in range(len(table[0])):
        curr = ord(table[0][j])
        for i in range(1, len(table)):
            c = ord(table[i][j])
            if c < curr:
                res += 1
                break
            curr = c
    return res

assert lexicographical_table([['c','b','a'],['d','a','f'],['g','h','i']]) == 1
assert lexicographical_table([['a','b','c','d','e','f']]) == 0
assert lexicographical_table([['z','y','x'],['w','v','u'],['t','s','r']]) == 3