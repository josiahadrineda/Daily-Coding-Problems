#TLE
def traverse_matrix(M, N):
    matrix = [[0 for _ in range(M)] for _ in range(N)]
    res = backtrack_matrix(0, 0, matrix, 0)
    return res

def backtrack_matrix(r, c, matrix, res):
    if r == len(matrix)-1 and c == len(matrix[0])-1:
        res += 1
    else:
        if is_valid(r, c, matrix):
            res = backtrack_matrix(r+1, c, matrix, res)
            res = backtrack_matrix(r, c+1, matrix, res)
    return res

def is_valid(r, c, matrix):
    return r < len(matrix) and c < len(matrix[0])

assert traverse_matrix(2, 2) == 2
assert traverse_matrix(7, 3) == 28
assert traverse_matrix(5, 5) == 70

#Accepted
def traverse_dp(M, N):
    matrix = [[0 for _ in range(M)] for _ in range(N)]
    matrix[0][0] = 1

    for i in range(1, M):
        matrix[0][i] = 1

    for i in range(1, N):
        matrix[i][0] = 1

    for i in range(1, N):
        for j in range(1, M):
            matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

    return matrix[-1][-1]

assert traverse_dp(2, 2) == 2
assert traverse_dp(7, 3) == 28
assert traverse_dp(5, 5) == 70