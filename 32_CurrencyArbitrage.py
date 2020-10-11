#Bellman-Ford Algorithm for Graph Traversal and Cycle Detection
from math import log

def currency_arbitrage(table):
    w = [[-log(edge) for edge in row] for row in table]
    dist = [float('inf')] * len(w)
    dist[0] = 0
    for _ in range(len(w)-1):
        for u in range(len(w)):
            for v in range(len(w)):
                dist[u] = min(dist[u], dist[v]+w[u][v])
    
    for u in range(len(w)):
        for v in range(len(w)):
            if dist[u] > dist[v] + w[u][v]:
                return True
    return False

exchange_rates = [[1,2],[2,1]]
print(currency_arbitrage(exchange_rates))