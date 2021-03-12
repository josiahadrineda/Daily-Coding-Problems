"""
Comments:
 - Probably could've checked whether the starting state was solvable or not.
   Didn't know that was a thing...
"""

from random import randint
from itertools import chain
from copy import deepcopy
from heapq import heappush, heappop

class Board:
    """A class for a SQUARE game board.
    """
    def __init__(self, N, bo=[]):
        assert N > 0, 'The side length of a board must be greater than 0.'
        bo = [[""] * N for _ in range(N)] if not bo else bo
        r, c = len(bo), len(bo[0])
        assert r == c == N, 'R and C must be equal to N.'

        self.N = N
        self.bo = bo

    def __eq__(self, other):
        assert isinstance(other, Board), 'OTHER must be an instance of the Board class.'
        return self.bo == other.bo

    def __lt__(self, other):
        return 0

    def __hash__(self):
        bo_tuple = tuple([tuple(r) for r in self.bo])
        return hash(bo_tuple)

    def print_board(self):
        for r in range(self.N):
            for c in range(self.N):
                print(self.get(r, c) + ' ', end='')
            print()
        print()

    def is_valid(self, r, c):
        return 0 <= r < self.N and 0 <= c < self.N

    def get(self, r, c):
        assert self.is_valid(r, c), 'R and/or C are out of bounds.'

        return self.bo[r][c]

    def put(self, r, c, val):
        assert self.is_valid(r, c), 'R and/or C are out of bounds.'

        self.bo[r][c] = val

    def index(self, el):
        for r in range(self.N):
            for c in range(self.N):
                if self.get(r, c) == el:
                    return (r, c)
        return (-1, -1)

    def swap(self, r1, c1, r2, c2):
        assert self.is_valid(r1, c1), 'R1 and/or C1 are out of bounds.'
        assert self.is_valid(r2, c2), 'R2 and/or C2 are out of bounds.'

        el1, el2 = self.get(r1, c1), self.get(r2, c2)
        self.put(r1, c1, el2)
        self.put(r2, c2, el1)

class N_Puzzle:
    """Note that N is equal to the SIDE LENGTH of the board.
    """
    def __init__(self, N):
        assert N > 1, 'The side length of a board must be greater than 1.'

        self.N = N
        self.bo = Board(N)
        self.ideal_bo_flattened = [str(x) for x in range(1, N**2)] + ['_']

    def populate(self):
        cells = self.ideal_bo_flattened
        for r in range(self.N):
            for c in range(self.N):
                self.bo.put(r, c, cells.pop(0))

    def shuffle(self, iter=1000):
        for _ in range(iter):
            r1, c1 = randint(0, self.N - 1), randint(0, self.N - 1)
            r2, c2 = randint(0, self.N - 1), randint(0, self.N - 1)
            while r1 == c1 and r2 == c2:
                r1, c1 = randint(0, self.N - 1), randint(0, self.N - 1)
                r2, c2 = randint(0, self.N - 1), randint(0, self.N - 1)
            self.bo.swap(r1, c1, r2, c2)


    def valid_board(self, bo):
        return sorted(list(chain(*bo.bo))) == self.ideal_bo_flattened

    def solve(self, goal, start=None, swaps=0):
        """Solves an N^2-1 - Puzzle with starting and goal states GOAL and START.
        This puzzle takes place on an NxN board and N^2 - 1 tiles (one space). The
        player must reach the end state by shifting the tiles around one space at a
        time in any of the four axial directions.
        """
        start = self.bo if not start else start
        if start != self.bo: assert self.valid_board(start), 'Starting state is not valid.'
        assert self.valid_board(goal), 'Goal state is not valid.'

        def f_score(bo, goal, swaps):
            """A heuristic for a board state.
            """

            def h_score():
                """Sum of the distances between BO's cells and GOAL's cells.
                """

                def dist(x1, y1, x2, y2):
                    return abs(x1 - x2) + abs(y1 - y2)

                tot = 0
                for r1 in range(self.N):
                    for c1 in range(self.N):
                        cell = bo.get(r1, c1)
                        r2, c2 = goal.index(cell)
                        tot += dist(r1, c1, r2, c2)
                return tot

            def g_score():
                """The number of swaps so far.
                """

                return swaps

            return h_score() + g_score()

        self.populate()
        self.shuffle()

        # Format of a tuple in the PQ: (blank_pos, f_score, # swaps, board)
        pq, visited, parents = [], set(), {}
        start_blank_pos = start.index('_')
        start_copy, start_swaps = Board(self.N, deepcopy(start.bo)), 0
        start_f = f_score(start_copy, goal, start_swaps)
        heappush(pq, (start_f, start_blank_pos, start_copy, start_swaps))
        parents[start_copy] = None

        while pq:
            f, p, b, s = heappop(pq)
            if b == goal:
                break

            r, c = p
            visited.add(hash(b))
            for nr, nc in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                if b.is_valid(nr, nc):
                    b.swap(r, c, nr, nc)
                    if hash(b) not in visited:
                        np = (nr, nc)
                        nb, ns = Board(self.N, deepcopy(b.bo)), s + 1
                        nf = f_score(nb, goal, ns)
                        heappush(pq, (nf, np, nb, ns))

                        parents[nb] = b
                    b.swap(r, c, nr, nc)

        if b != goal:
            print('Impossible solve.')
            return

        res = []
        while b:
            res.insert(0, b)
            b = parents[b]
        for bo in res:
            bo.print_board()

""" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - """

np = N_Puzzle(3)
# Omit if want to test on a random starting state
start = Board(3, [['1', '3', '2'], ['5', '4', '_'], ['7', '8', '6']])
goal = Board(3, [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '_']])
np.solve(goal, start=start)