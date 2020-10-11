def determine_nondecreasing(arr):
    outliers = 0
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            outliers += 1
    return outliers <= 1

assert determine_nondecreasing([10,5,7]) == True
assert determine_nondecreasing([10,5,1]) == False