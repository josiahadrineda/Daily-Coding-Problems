import time

def runtime(func):
    def call(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Runtime for {}: {}s".format(func.__name__, end-start))
        return
    return call

def prod(nums):
    x = 1
    for num in nums:
        x *= num
    return x

@runtime
def product(nums):
    j, sol = 0, []

    #Base case
    if 0 in nums:
        return 0

    for i in range(1, len(nums)+1):
        num = prod(nums[:j]) * prod(nums[i:])
        sol.append(num)
        j += 1
    print("Solution: {}".format(sol))
    return sol

import random

nums = [random.randint(1,9) for i in range(9)]
print("Nums: {}".format(nums))
product(nums)