def attack_bishops(M, bishops):
    res = 0
    if M == 0 or not bishops or len(bishops) == 0:
        return res

    bo = [[0 for _ in range(M)] for _ in range(M)]
    for bishop in bishops:
        r,c = bishop
        bo[r][c] = 1

    for bishop in bishops:
        r,c = bishop
        res += dfs(r+1, c-1, 0, bo, M, res)
        res += dfs(r+1, c+1, 1, bo, M, res)
    return res

def dfs(r, c, dir, bo, M, res):
    if r < 0 or r >= M or c < 0 or c >= M:
        return 0
    elif bo[r][c] == 1:
        return 1
    else:
        if dir == 0:
            res = dfs(r+1, c-1, 0, bo, M, res)
        else:
            res = dfs(r+1, c+1, 1, bo, M, res)
        return res

assert attack_bishops(5, [(0,0),(1,2),(2,2),(4,0)]) == 2
assert attack_bishops(3, [(0,1),(1,0),(1,2),(2,1)]) == 4