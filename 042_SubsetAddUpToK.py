#I still don't know how this recursive solution is achieved. Perhaps revisit this at a later date.
def get_subset_for_sum(arr, k):
    if len(arr) == 0:
        return None

    if arr[0] == k:
        return [arr[0]]

    with_first = get_subset_for_sum(arr[1:], k - arr[0])
    if with_first:
        return [arr[0]] + with_first
    else:
        return get_subset_for_sum(arr[1:], k)

from itertools import combinations

def brute_force_subset(arr, k):
    for i in range(len(arr)+1):
        for combo in combinations(arr, i):
            if sum(combo) == k:
                return list(combo)
    return None

def bottom_up_dp_subset(arr, k):
    dp = [[False] * (k + 1) for _ in range(len(arr))]
    for i in range(len(arr)):
        dp[i][0] = True
        for j in range(1, k + 1):
            if j == arr[i]:
                dp[i][j] = True
            elif j < arr[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i]]
    for line in dp:
        print(line)
    return dp[-1][-1]

arr = [2,3,7,8,10]
k = 14
#rint(bottom_up_dp_subset(arr, k))

from itertools import permutations

for perm in permutations('ginger'):
    print(perm)