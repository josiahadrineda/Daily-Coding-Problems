def measure_water(height):
    if len(height) <= 2:
        return 0
    
    res = 0
    for i in range(1, len(height)-1):
        max_l_height = max(height[:i])
        max_r_height = max(height[i+1:])
        tot_height = min(max_l_height, max_r_height)
        water_amt = tot_height - height[i]
        
        res += water_amt if water_amt > 0 else 0
    return res

#Driver code
assert measure_water([2,1,2]) == 1
assert measure_water([3,0,1,3,0,5]) == 8
assert measure_water([2,1,0]) == 0