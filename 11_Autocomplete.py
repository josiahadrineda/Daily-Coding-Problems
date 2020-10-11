def autocomplete(s, dic):
    if not s:
        return dic
        
    res = []
    for word in dic:
        if s in word:
            res.append(word)
    return res

s = "do"
dic = ["dog", "deer", "deal"]
print(autocomplete(s, dic))