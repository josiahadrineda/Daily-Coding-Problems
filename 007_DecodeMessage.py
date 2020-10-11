def num_ways(s):
    if s == '0':
        return 0

    dp = [0 for i in range(len(s)+1)]

    dp[0] = 1
    dp[1] = 1 if s[0] != '0' else 0

    for i in range(1, len(s)):
        if s[i] != '0':
            dp[i+1] += dp[i]
        if s[i-1] != '0' and 10 <= int(s[i-1:i+1]) <= 26:
            dp[i+1] += dp[i-1]
    return dp[len(s)]

s = '123456789'
print(num_ways(s))