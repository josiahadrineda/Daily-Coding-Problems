#Look at proper solution and adapt

from copy import deepcopy
from sys import exit

class Sudoku:
    def __init__(self, bo):
        self.bo = bo

    def print_board(self, bo):
        print('-------------------')
        for i in range(len(bo)):
            print('|', end='')
            for j in range(len(bo[0])):
                if bo[i][j] != 0:
                    print(str(bo[i][j]) + '|', end='')
                else:
                    print(' |', end='')
            print()
            if (i-2) % 3 == 0:
                print('-------------------')
        print()

    def solve(self):
        bo = deepcopy(self.bo)
        self.print_board(bo)

        nums = [i for i in range(1,10)]

        locked_tiles = []
        for i in range(len(bo)):
            for j in range(len(bo[0])):
                if bo[i][j] != 0:
                    locked_tiles.append((i,j))

        self.solve_helper(bo, locked_tiles, 0, 0)
        print("No solution found for current board.")

    def solve_helper(self, bo, locked_tiles, r, c):
        if r == len(bo):
            self.print_board(bo)
            exit(0)
        elif c == len(bo[0]):
            self.solve_helper(bo, locked_tiles, r+1, 0)
        elif (r, c) in locked_tiles:
            self.solve_helper(bo, locked_tiles, r, c+1)
        else:
            for i in range(1, 10):
                bo[r][c] = i
                if self.is_valid(bo, i, r, c):
                    self.solve_helper(bo, locked_tiles, r, c+1)
                bo[r][c] = 0

    def is_valid(self, bo, num, r, c):
        #Check row
        for i in range(len(bo)):
            if i != c and bo[r][i] == num:
                return False

        #Check col
        for i in range(len(bo[0])):
            if i != r and bo[i][c] == num:
                return False

        #Check subgrid
        if r < 3 and c < 3:
            for i,j in (0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2):
                if i != r and j != c and bo[i][j] == num:
                    return False
        elif r < 3 and 3 <= c < 6:
            for i,j in (0,3), (0,4), (0,5), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5):
                if i != r and j != c and bo[i][j] == num:
                    return False
        elif r < 3 and 6 <= c < 9:
            for i,j in (0,6), (0,7), (0,8), (1,6), (1,7), (1,8), (2,6), (2,7), (2,8):
                if i != r and j != c and bo[i][j] == num:
                    return False
        elif 3 <= r < 6 and c < 3:
            for i,j in (3,0), (3,1), (3,2), (4,0), (4,1), (4,2), (5,0), (5,1), (5,2):
                if i != r and j != c and bo[i][j] == num:
                    return False
        elif 3 <= r < 6 and 3 <= c < 6:
            for i,j in (3,3), (3,4), (3,5), (4,3), (4,4), (4,5), (5,3), (5,4), (5,5):
                if i != r and j != c and bo[i][j] == num:
                    return False
        elif 3 <= r < 6 and 6 <= c < 9:
            for i,j in (3,6), (3,7), (3,8), (4,6), (4,7), (4,8), (5,6), (5,7), (5,8):
                if i != r and j != c and bo[i][j] == num:
                    return False
        elif 6 <= r < 9 and c < 3:
            for i,j in (6,0), (6,1), (6,2), (7,0), (7,1), (7,2), (8,0), (8,1), (8,2):
                if i != r and j != c and bo[i][j] == num:
                    return False
        elif 6 <= r < 9 and 3 <= c < 6:
            for i,j in (6,3), (6,4), (6,5), (7,3), (7,4), (7,5), (8,3), (8,4), (8,5):
                if i != r and j != c and bo[i][j] == num:
                    return False
        elif 6 <= r < 9 and 6 <= c < 9:
            for i,j in (6,6), (6,7), (6,8), (7,6), (7,7), (7,8), (8,6), (8,7), (8,8):
                if i != r and j != c and bo[i][j] == num:
                    return False
        return True

#Driver code
"""
Template:
     [[0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0]]
"""

bo = [[4,0,0,1,0,5,0,0,7],
      [0,0,1,0,0,0,9,0,0],
      [0,7,0,0,6,0,0,1,0],
      [7,0,0,6,0,2,0,0,9],
      [0,0,5,0,0,0,3,0,0],
      [1,0,0,7,0,3,0,0,8],
      [0,9,0,0,1,0,0,2,0],
      [0,0,8,0,0,0,6,0,0],
      [6,0,0,4,0,9,0,0,1]]

sudoku = Sudoku(bo)
sudoku.solve()