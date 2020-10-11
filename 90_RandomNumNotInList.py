from random import randint
from collections import defaultdict

def generate_rand(n, arr):
    possible_nums = [i for i in range(n)]
    for el in arr:
        possible_nums.remove(el)
    
    k = len(possible_nums)
    for i in range(k):
        if randint(0, i) == 0:
            rand_num = possible_nums[i]
    return rand_num

num_to_freq = defaultdict(int)

num_trials = 1000000
n = 11
arr = [1,3,5,7,9]
for _ in range(num_trials):
    num_to_freq[generate_rand(n, arr)] += 1

error = 0.05
goal = 1 / len(num_to_freq.values())
for k,v in num_to_freq.items():
    assert goal - goal*error <= v / num_trials <= goal + goal*error