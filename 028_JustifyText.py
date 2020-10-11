def justify_text(words, k):
    res = []
    """
    determine lengths of words
    minimize spaces, aka maximize lengths of words according to k
    if more than one word in string, pad from left (between two words)
    if only one word, pad from right (whitespace)
    """
    while words:
        s = []
        cnt = 0
        while cnt <= k-len(s):
            try:
                cnt += len(words[0])
            except:
                break
            if cnt <= k-len(s):
                s.append(words[0])
                words.pop(0)
            else:
                cnt -= len(words[0])
                break
        
        num_spaces = k-cnt
        holes = len(s)-1 if len(s)-1 else 1
        space_cnt = num_spaces // holes
        if num_spaces % holes == 0:
            for j in range(holes):
                s[j] += ' ' * space_cnt
        else:
            """
            spaces do not evenly divide into holes
            """
            extra = num_spaces % holes
            j = 0
            while j < extra:
                s[j] += ' ' * (space_cnt+1)
                num_spaces -= (space_cnt+1)
                j += 1
            
            while j < len(s)-1:
                s[j] += ' ' * space_cnt
                j += 1
        
        res.append(''.join(s))
    return res

words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
print(justify_text(words, 32))