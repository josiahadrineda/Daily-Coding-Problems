def longest_substring(s, k):
    if len(s) < k:
        return -1
    elif len(set(s)) < k:
        return -1
    elif s and k == 1:
        return 1
    
    max_len = 0
    l, r = 0, 1
    length = len(s)
    while r <= length:
        if len(set(s[l:r])) <= k:
            max_len = max(max_len, len(s[l:r]))
            r += 1
        else:
            while len(set(s[l:r])) > k:
                l += 1
    return max_len

#Driver code
from random import randint

s = ""
s = s.join([chr(randint(97, 122)) for i in range(100)])
k = 10
print(s, k)
print(longest_substring(s, k))