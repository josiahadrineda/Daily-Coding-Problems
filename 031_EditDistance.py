def edit_distance(s, t):
    if len(s) < len(t):
        s += ' ' * (len(t)-len(s))
    elif len(s) > len(t):
        t += ' ' * (len(s)-len(t))

    res = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            res += 1
    return res

s = "kitten"
t = "sit"
print(edit_distance(s, t))

#New and improved edit distance alg
from functools import lru_cache

def recur_edit_distance(s, t):
    @lru_cache(maxsize=None)
    def helper(i, j):
        if i == len(s):
            return len(t) - j
        elif j == len(t):
            return len(s) - i
        
        if s[i] == t[j]:
            return helper(i+1, j+1)
        else:
            return 1 + min(helper(i+1, j+1), helper(i+1, j), helper(i, j+1))
    return helper(0, 0)

assert recur_edit_distance("insertion", "execution") == 5