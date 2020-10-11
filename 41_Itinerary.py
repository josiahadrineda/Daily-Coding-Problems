"""Euler's Path Finding Algorithm"""

from collections import defaultdict

def itinerary(flights, node):
    flights.sort()

    dic = defaultdict(list)
    for s,e in flights:
        dic[s].append(e)

    res = []
    dfs(node, dic, res)
    return res if len(res) == len(flights)+1 else None

def dfs(curr, dic, res):
    while dic[curr]:
        next_flight = dic[curr].pop(0)
        dfs(next_flight, dic, res)
    res.insert(0, curr)

flights = [('SFO','HKO'),('YYZ','SFO'),('YUL','YYZ'),('HKO','ORD')]
print(itinerary(flights, 'YUL'))