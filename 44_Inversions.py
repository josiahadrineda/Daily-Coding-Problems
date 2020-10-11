def count_inversions(arr):
    _, inversions = merge_sort(arr)
    return inversions

def merge_sort(arr):
    if len(arr) == 1:
        return arr, 0

    mid = len(arr) // 2
    l, r = arr[:mid], arr[mid:]

    merged_arr, inversions = merge_util(merge_sort(l), merge_sort(r))
    return merged_arr, inversions

def merge_util(l, r):
    merged_arr = []

    a, a_inv = l
    b, b_inv = r
    inversions = a_inv + b_inv

    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged_arr.append(a[i])
            i += 1
        else:
            merged_arr.append(b[j])
            inversions += len(a[i:])
            j += 1
    
    while i < len(a):
        merged_arr.append(a[i])
        i += 1
    
    while j < len(b):
        merged_arr.append(b[j])
        j += 1
    
    return merged_arr, inversions

arr = [5,4,3,2,1]
print(count_inversions(arr))

def reverse_pairs(nums):
    if not nums or len(nums) == 0:
        return 0

    return merge_helper(nums, 0, len(nums)-1)

def merge_helper(nums, s, e):
    if s >= e:
        return 0

    count = 0
    m = (s + e) // 2

    count += merge_helper(nums, s, m)
    count += merge_helper(nums, m+1, e)

    l = s
    r = m + 1
    while l <= m and r <= e:
        if nums[l] > nums[r]:
            count += m - l + 1
            r += 1
        else:
            l += 1
    
    nums[s:m+1] = sorted(nums[s:m+1])
    return count

arr = [5,4,3,2,1]
print(reverse_pairs(arr))