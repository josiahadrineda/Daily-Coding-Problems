def binary_search(arr, k):
    if arr[0] > arr [-1]:
        res = binary_search(arr[::-1], k)
        res = len(arr) - res - 1 if res else None
        return res

    l,r = 0, len(arr)-1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            r = mid - 1
        else:
            l = mid + 1
    return None

arr = [1,2,3,4,5]
assert binary_search(arr, 4) == 3
assert binary_search(arr[::-1], 4) == 1
assert binary_search(arr, 6) == None
assert binary_search(arr[::-1], 0) == None