def partition(arr):
    goal = sum(arr) / 2
    if not arr or len(arr) == 0:
        return False
    elif int(goal) != goal:
        return False
    
    arr.sort()
    l,r = 0, len(arr)
    while l <= r:
        mid = (l + r) // 2
        l_list, r_list = arr[:mid], arr[mid:]
        l_sum, r_sum = sum(l_list), sum(r_list)
        if l_sum == r_sum:
            return l_list, r_list
        elif l_sum < r_sum:
            l += 1
        else:
            r -= 1
    return False

print(partition([15, 5, 20, 10, 35, 15, 10]))
print(partition([15, 5, 20, 10, 35]))