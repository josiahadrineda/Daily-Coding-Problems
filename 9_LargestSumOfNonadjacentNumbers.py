def nonadjacent_sum(nums):
    #Equivalent to Leetcode's House Robber problem
    #Use DP
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return max(nums[0], nums[1])

    dp = []
    dp.append(nums[0])
    dp.append(max(nums[0], nums[1]))

    for i in range(2, len(nums)):
        dp.append(max(nums[i] + dp[i-2], dp[i-1]))
    print(dp)
    return dp[len(nums)-1]
nums = [5,1,1,5]
print(nonadjacent_sum(nums))