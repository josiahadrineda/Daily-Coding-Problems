def minimum_classrooms(times):
    times.sort()
    res = 0

    while times:
        curr = times.pop(0)
        _, curr_end = curr

        res += 1
        
        for next_start, _ in times:
            if next_start > curr_end:
                times.remove((next_start, _))
    
    return res

#Driver code
times = [(0,50),(2,60),(51,80),(7,120),(130,180)]
print(minimum_classrooms(times))