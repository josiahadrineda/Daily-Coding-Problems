def encode(s):
    res = ""
    curr = s[0]
    freq = 1
    i = 1
    while i < len(s):
        if s[i] == curr:
            freq += 1
        else:
            res += str(freq) + curr
            curr = s[i]
            freq = 1
        i += 1
    res += str(freq) + curr
    return res

def decode(s):
    res = ""
    for i in range(1, len(s), 2):
        res += s[i] * int(s[i-1])
    return res

s = "AAAABBBCCDAA"
print(encode(s))
print(decode(encode(s)))