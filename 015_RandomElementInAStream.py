import random

def get_random_element(nums):
    res, max_num = 0, 0
    for num in nums:
        rand = random.random()
        if rand > max_num:
            max_num = rand
            res = num
    return res

nums = [random.randint(1, pow(10, 5)) for i in range(pow(10, 5))]
print(get_random_element(nums))