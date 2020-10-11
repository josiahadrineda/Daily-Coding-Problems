def phone_number_combinations(s):
    d = {'2':['a','b','c'],
         '3':['d','e','f'],
         '4':['g','h','i'],
         '5':['j','k','l'],
         '6':['m','n','o'],
         '7':['p','q','r','s'],
         '8':['t','u','v'],
         '9':['w','x','y','z']}

    res = []
    res = backtrack(res, s, d, '', 0)
    return res

def backtrack(res, s, d, curr, ind):
    if len(curr) == len(s):
        res.append(curr)
    else:
        for char in d[s[ind]]:
            curr += char
            res = backtrack(res, s, d, curr, ind+1)
            curr = curr[:-1]
    return res

assert 'jnsa' in phone_number_combinations('5672')