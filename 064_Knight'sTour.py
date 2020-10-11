#Supposed to be NxN so yeet
def knights_tour(N):
    res = 0
    for i in range(N):
        for j in range(N):
            matrix = [[None for _ in range(N)] for _ in range(N)]
            matrix[i][j] = 0
            res += knights_backtrack(matrix, [(i,j)], N)
    return res

def knights_backtrack(matrix, path, N):
    if len(path) == N**2:
        return 1
    else:
        cnt = 0
        prev_r,prev_c = path[-1]
        for r,c in valid_moves(matrix, prev_r, prev_c, N):
            path.append((r,c))
            matrix[r][c] = len(path)
            cnt += knights_backtrack(matrix, path, N)
            path.pop()
            matrix[r][c] = None
        return cnt

def valid_moves(matrix, r, c, N):
    deltas = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
    all_moves = [(r+delta_r,c+delta_c) for delta_r,delta_c in deltas]
    return [(r,c) for r,c in all_moves if is_valid(matrix, r, c, N)]

def is_valid(matrix, r, c, N):
    return 0 <= r < N and 0 <= c < N and matrix[r][c] == None

assert knights_tour(1) == 1
assert knights_tour(2) == 0
assert knights_tour(3) == 0
assert knights_tour(4) == 0
assert knights_tour(5) == 1728