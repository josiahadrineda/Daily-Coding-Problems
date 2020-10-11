import time
def display_and_runtime(f):
    def helper(*args, **kwargs):
        s = time.time()
        print("Result of {}: {}".format(f.__name__, f(*args, **kwargs)))
        e = time.time()
        runtime = (e-s) * 1000
        print("Runtime of {}: {}ms".format(f.__name__, runtime))
        print()
        return
    return helper

#How to implement given any set of nums for x???

@display_and_runtime
def count_ways_recur(x, n):
    return recur_helper(x, n)

def recur_helper(x, n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    return sum([recur_helper(x, n-num) for num in x])

from collections import defaultdict

@display_and_runtime
def count_ways_dp_top_down(x, n): #With memoization
    visited = defaultdict(int)
    return dp_helper(x, n, visited)

def dp_helper(x, n, visited):
    if n < 0:
        return 0
    elif n == 0:
        return 1

    if visited[n] > 0:
        return visited[n]
    visited[n] = sum([dp_helper(x, n-num, visited) for num in x])
    return visited[n]

#Driver code
x = [1,2,5]
n = 5
#count_ways_recur(x, n)  #Extremely inefficient
count_ways_dp_top_down(x, n)    #A lot more reliable