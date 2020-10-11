import time

class Matrix:
    def __init__(self, M, N, matrix):
        self.M = M
        self.N = N
        self.matrix = matrix
    
    def print_matrix(self, matrix):
        for i in range(self.M):
            for j in range(self.N):
                print(matrix[i][j], end=' ')
            print()
        print()

    def solve(self, s, e):
        self.print_matrix(self.matrix)

        sy, sx = s
        ey, ex = e
        if self.matrix[sy][sx] or self.matrix[ey][ex]:
            return None
        
        res = [[0 for i in range(self.M)] for j in range(self.N)]
        q = []
        visited = set()
        q.append((sy, sx))
        visited.add((sy, sx))
        while q:
            time.sleep(1)
            self.print_matrix(res)
            curr_y, curr_x = q.pop(0)
            if curr_y == ey and curr_x == ex:
                break

            if curr_y < self.N-1:   #Down
                if self.matrix[curr_y+1][curr_x] == 0 and (curr_y+1, curr_x) not in visited:
                    res[curr_y+1][curr_x] = res[curr_y][curr_x] + 1
                    q.append((curr_y+1, curr_x))
                    visited.add((curr_y+1, curr_x))
            if curr_y > 0:          #Up
                if self.matrix[curr_y-1][curr_x] == 0 and (curr_y-1, curr_x) not in visited:
                    res[curr_y-1][curr_x] = res[curr_y][curr_x] + 1
                    q.append((curr_y-1, curr_x))
                    visited.add((curr_y-1, curr_x))
            if curr_x < self.M-1:   #Right
                if self.matrix[curr_y][curr_x+1] == 0 and (curr_y, curr_x+1) not in visited:
                    res[curr_y][curr_x+1] = res[curr_y][curr_x] + 1
                    q.append((curr_y, curr_x+1))
                    visited.add((curr_y, curr_x+1))
            if curr_x > 0:          #Left
                if self.matrix[curr_y][curr_x-1] == 0 and (curr_y, curr_x-1) not in visited:
                    res[curr_y][curr_x-1] = res[curr_y][curr_x] + 1
                    q.append((curr_y, curr_x-1))
                    visited.add((curr_y, curr_x-1))
        if res[ex][ey] == 0:
            return None
        return res[ex][ey]

#Driver code
from random import randint

m = Matrix(5, 5, [[0,0,0,0,0],
                  [1,1,1,1,0],
                  [0,0,0,0,0],
                  [0,1,1,1,1],
                  [0,0,0,0,0]])
print(m.solve((0,0), (4,4)))