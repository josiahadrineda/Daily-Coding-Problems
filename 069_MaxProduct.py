def max_product(arr):
    arr.sort()
    a = arr[-1] * arr[-2] * arr[-3]
    b = arr[0] * arr[1] * arr[-1]
    return max(a,b)

assert max_product([-10,-10,5,2]) == 500
assert max_product([-10, 10, 5, 2]) == 100