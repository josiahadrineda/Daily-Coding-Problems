def max_vals(nums, k):
    if k == 1:
        return nums

    for i in range(k-1, len(nums)):
        nums[i-k+1] = max(nums[i-j] for j in range(k))
    return nums[:-k+1]

#Driver code
from random import randint

nums = [randint(1, 9) for i in range(20)]
print(nums)

k = 7
print(max_vals(nums, k))