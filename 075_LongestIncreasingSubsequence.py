def longest_increasing_subsequence(nums):
    if not nums or len(nums) == 0:
        return 0
    
    subsequence = [-1] * len(nums)
    ind = 0

    dp = [1] * len(nums)
    max_len = 1
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i] and dp[j] >= dp[i]:
                dp[i] = max(dp[i], dp[j]+1)
                subsequence[i] = j
        
        if dp[i] > max_len:
            max_len = dp[i]
            ind = i

    # Print subsequence for convenience
    subseq_list = []
    while ind != -1:
        subseq_list.insert(0, nums[ind])
        ind = subsequence[ind]
    print(subseq_list)
    return max_len

assert longest_increasing_subsequence([0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]) == 6
assert longest_increasing_subsequence([1,3,6,7,9,4,10,5,6]) == 6
assert longest_increasing_subsequence([10,9,2,5,3,7,101,18]) == 4