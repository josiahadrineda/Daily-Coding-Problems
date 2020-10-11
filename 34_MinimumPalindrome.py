def get_nearest_palindrome(s):
    l = r = float('inf')
    j = len(s)-1
    for i in range(len(s)):
        if s[:i+1][::-1] in s:
            addition = len(s) - (i+1)
            l = min(l, addition)
        if s[j:][::-1] in s:
            addition = len(s) - (len(s)-j)
            r = min(r, addition)
        j -= 1

    if l <= r:
        return s[len(s)-l:][::-1] + s
    else:
        return s + s[:r][::-1]

assert get_nearest_palindrome("racecar") == "racecar"
assert get_nearest_palindrome("google") == "elgoogle"
assert get_nearest_palindrome("ogle") == "elgogle"
assert get_nearest_palindrome("elgoog") == "elgoogle"
assert get_nearest_palindrome("race") == "ecarace"

def is_palindrome(s):
    return s[::-1] == s

def palindrome_recur(s):
    if is_palindrome(s):
        return s
    
    if s[0] == s[-1]:
        return s[0] + palindrome_recur(s[1:-1]) + s[-1]
    else:
        p1 = s[0] + palindrome_recur(s[1:]) + s[0]
        p2 = s[-1] + palindrome_recur(s[:-1]) + s[-1]

        return p1 if p1 < p2 else p2

print(palindrome_recur("abcd"))