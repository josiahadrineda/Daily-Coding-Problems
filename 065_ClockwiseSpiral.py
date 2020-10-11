def print_clockwise_spiral(matrix):
    M,N = len(matrix[0]), len(matrix)
    visited = []

    dirs = {0:(0,1), 1:(1,0), 2:(0,-1), 3:(-1,0)}
    curr_dir = 0
    pos = (0,0)
    cnt = 0
    while True:
        r,c = pos
        if cnt == M * N - 1:
            print(matrix[r][c])
            break

        visited.append((r,c))
        delta_r, delta_c = dirs[curr_dir]
        if valid_pos(M, N, r, c, delta_r, delta_c, visited):
            pos = (r + delta_r, c + delta_c)
            
            print(matrix[r][c])
            cnt += 1
        else:
            curr_dir = (curr_dir + 1) % 4

def valid_pos(M, N, r, c, delta_r, delta_c, visited):
    return 0 <= r + delta_r < N and 0 <= c + delta_c < M and \
           (r + delta_r, c + delta_c) not in visited

matrix = [[1, 2, 3, 4, 5 ],
          [6, 7, 8, 9, 10],
          [11,12,13,14,15],
          [16,17,18,19,20]]
print_clockwise_spiral(matrix)