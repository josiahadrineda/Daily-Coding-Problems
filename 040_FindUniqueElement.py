def find_unique_element(arr):
    unique = set(arr)
    return int((3 * sum(unique) - sum(arr)) / 2)

arr = [1,1,1,2,2,2,3,4,4,4]
print(find_unique_element(arr))