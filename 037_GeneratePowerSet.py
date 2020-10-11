from itertools import combinations

def generate_power_set(arr):
    res = []
    for i in range(len(arr)+1):
        for combo in combinations(arr, i):
            res.append(combo)
    return res

def power_set_bits(arr):
    res = []
    l = len(arr)
    for i in range(pow(2, l)):
        _ = []
        for j in range(l):
            if (i & (1 << j)) > 0:
                _.append(arr[j])
        res.append(_)
    return res

arr = [12,1,61,5,9,2]
print(power_set_bits(arr))

#THIS IS WRONG
#FIX IT