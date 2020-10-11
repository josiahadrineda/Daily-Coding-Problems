def is_palindrome(s):
    return s == s[::-1]

def find_longest(s):
    if not s or is_palindrome(s):
        return s
    
    s1 = find_longest(s[1:])
    s2 = find_longest(s[:-1])
    return s1 if len(s1) >= len(s2) else s2

s = "cbbd"
print(find_longest(s))