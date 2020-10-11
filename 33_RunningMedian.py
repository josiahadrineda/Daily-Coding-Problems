def running_median(arr):
    res = []
    for i in range(1, len(arr)+1):
        curr = sorted(arr[:i])
        if i % 2 == 1:
            res.append(curr[i//2])
        else:
            med = (curr[i//2 - 1] + curr[i//2]) / 2
            if int(med) == med:
                res.append(int(med))
            else:
                res.append(med)
    return res

import heapq as hq

def running_median_heap(arr):
    res, minheap, maxheap = [], [], []
    for num in arr:
        hq.heappush(minheap, num)
        if len(minheap) > len(maxheap)+1:
            el = hq.heappop(minheap)
            hq.heappush(maxheap, -el)
        
        if len(minheap) == len(maxheap):
            med = (minheap[0] - maxheap[0]) / 2
            if int(med) == med:
                med = int(med)
        else:
            med = minheap[0]
        res.append(med)
        print(minheap, maxheap)
    return res

nums = [1,2,3,4,5]
print(running_median(nums))
print(running_median_heap(nums))