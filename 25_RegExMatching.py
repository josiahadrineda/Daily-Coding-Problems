#0 = False, 1 = True
def match(s, p):
    ls, lp= len(s), len(p)
    if (not p or lp == 0) and s:
        return 0

    dp = [[0 for i in range(lp+1)] for j in range(ls+1)]
    dp[0][0] = 1
    for i in range(len(dp)):
        for j in range(1, len(dp[0])):
            if i == 0:
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-2]
            else:
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    if dp[i][j-2]:
                        dp[i][j] = 1
                    elif dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.'):
                        dp[i][j] = 1
    
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            print(dp[i][j], end=' ')
        print()
    print()

    return dp[ls][lp]

s = "ablmy"
p = "a*b.*y"
print(match(s, p))