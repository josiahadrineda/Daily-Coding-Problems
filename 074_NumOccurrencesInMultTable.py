def num_occurrences(N, X):
    res = 0
    for i in range(1, N+1):
        if i <= X <= N*i and X % i == 0:
            res += 1
    return res

assert num_occurrences(6,12) == 4
assert num_occurrences(6, 20) == 2
assert num_occurrences(6, 36) == 1