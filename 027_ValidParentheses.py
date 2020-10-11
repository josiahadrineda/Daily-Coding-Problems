def is_valid(s):
    if not s:
            return True
    elif len(s) % 2 == 1:
        return False
    
    """
    while "()" in s or "[]" in s or "{}" in s:
        s = s.replace("()", "").replace("[]", "").replace("{}", "")
    return not s
    """

    res = ""
    for c in s:
        res += c
        while "()" in res or "[]" in res or "{}" in res:
            res = res.replace("()", "").replace("[]", "").replace("{}", "")
    return not res

s = "()[]{"
print(is_valid(s))