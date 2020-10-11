def contiguous_subarray(arr):
    res = 0
    curr = 0
    for i in range(len(arr)):
        curr = max(curr + arr[i], 0)
        res = max(res, curr)
    return res

assert contiguous_subarray([34,-50,42,14,-5,86]) == 137