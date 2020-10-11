def partition(s, k):
    res = []
    end = 0
    while s:
        end += 1
        if end == len(s) or end == k:
            if end == k:
                while s[end] != ' ':
                    end -= 1
                    if end == 0:
                        return None
            res.append(s[:end])
            s = s[end+1:]
            end = 0
    return res

s = "The quick brown fox jumps over the lazy dog"
print(partition(s, 3))