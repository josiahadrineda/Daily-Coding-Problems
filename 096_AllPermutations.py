from itertools import permutations

def all_perms(digits):
    res = []
    for perm in permutations(digits):
        res.append(list(perm))
    return res

def all_perms_backtrack(digits):
    digits = sorted(digits)
    res = set()

    res = backtrack_helper(digits, [], res)
    res = [list(perm) for perm in sorted(res)]
    return res

def backtrack_helper(digits, curr_digits, res):
    if not digits:
        res.add(tuple(curr_digits.copy()))
    else:
        i = 0
        while i < len(digits):
            curr = digits.pop(i)
            curr_digits.append(curr)

            res = backtrack_helper(digits, curr_digits, res)

            digits.insert(i, curr)
            curr_digits.pop()
            i += 1
    return res