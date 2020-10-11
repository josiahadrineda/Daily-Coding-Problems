def reconstruct_sentence(dic, s):
    res = []
    i = 1
    while i < len(s)+1:
        if s[:i] in dic and (s[i:] == "" or prefix(dic, s[i:])):
            res.append(s[:i])
            s = s[i:]
            i = 1
        else:
            i += 1

    if s != "":
        res.append(s[i:])

    for word in res:
        if word not in dic:
            return None
    return res

def prefix(dic, s):
    i = 1
    while i < len(s)+1:
        if s[:i] in dic:
            return True
        i += 1
    return False

#Prints all available reconstructions as strings
#Can easily modify to only return one of these reconstructions

def reconstruct_recur(dic, s):
    if not s:
        return []
    return recur_helper(dic, s)

def recur_helper(dic, s):
    res = []
    for word in dic:
        if s.startswith(word):
            if s == word:
                res.append(word)
            else:
                ans = recur_helper(dic, s[len(word):])
                for el in ans:
                    res.append(word + ' '+ el)
    return res

#Driver code
dic = ["bird", "birds", "sin", "in", "a", "birdbath"]
s = "birdsinabirdbath"
print(reconstruct_sentence(dic, s))
print(reconstruct_recur(dic, s))