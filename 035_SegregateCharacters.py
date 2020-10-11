def segregate_chars(arr):
    lo = mid = 0
    hi = len(arr)-1
    while mid <= hi:
        if arr[mid] == 'R':
            arr[lo], arr[mid] = arr[mid], arr[lo]
            lo += 1
            mid += 1
        elif arr[mid] == 'G':
            mid += 1
        elif arr[mid] == 'B':
            arr[hi], arr[mid] = arr[mid], arr[hi]
            hi -= 1
    return arr

#Driver code
from random import randint

arr = [randint(1,3) for _ in range(10)]
for i in range(len(arr)):
    if arr[i] == 1:
        arr[i] = 'R'
    elif arr[i] == 2:
        arr[i] = 'G'
    else:
        arr[i] = 'B'
print(arr)
print(segregate_chars(arr))