def number_of_islands(matrix):
    res = 0
    islands = [(i,j) for j in range(len(matrix[0])) for i in range(len(matrix)) if matrix[i][j] == 1]
    while islands:
        bfs(matrix, islands)
        res += 1
    return res

def bfs(matrix, islands):
    i,j = islands.pop(0)
    for i,j in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
        if is_valid(matrix, islands, i, j):
            bfs(matrix, islands)

def is_valid(matrix, islands, i, j):
    return 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) and (i,j) in islands

assert number_of_islands([[1,0,0,0,0],[0,0,1,1,0],[0,1,1,0,0],[0,0,0,0,0],[1,1,0,0,1],[1,1,0,0,1]]) == 4
assert number_of_islands([[1,0,1],[0,0,0],[1,1,1]]) == 3
assert number_of_islands([[1,1,0,1,1],[1,1,0,1,1]]) == 2