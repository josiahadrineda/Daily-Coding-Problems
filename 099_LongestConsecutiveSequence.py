def longest_consecutive_sequence(nums):
    res = 0
    s = set(nums)

    for num in nums:
        if num - 1 not in s:
            curr = num
            streak = 1

            while curr + 1 in s:
                curr, streak = curr + 1, streak + 1

            res = max(res, streak)
    return res

assert longest_consecutive_sequence([]) == 0
assert longest_consecutive_sequence([100,200]) == 1
assert longest_consecutive_sequence([100,4,200,1,3,2]) == 4