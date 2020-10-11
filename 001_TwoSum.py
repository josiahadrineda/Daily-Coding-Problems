import time

def runtime(func):
    def call(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Runtime for {}: {}s".format(func.__name__, end-start))
        return
    return call

@runtime
def TwoSum(nums, k):
    s = set() #To avoid any dupes
    for num in nums:
        if k - num in s:
            print("{} + {} = {}".format(k-num, num, k))
            return True
        s.add(num)
    print("No two numbers add up to " + k + "...")
    return False

import random

nums = [random.randint(1, 9999) for i in range(9999)]
k = random.randint(3, 19997)
TwoSum(nums, k)