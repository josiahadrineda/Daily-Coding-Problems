from copy import deepcopy

def conway(points, k):
    bo = init_board(points)
    print("Starting board:")
    print_board(bo)
    for i in range(k):
        prev = deepcopy(bo)
        if len(bo) == 0:
            print("There are no longer any more living cells...")
            return

        expand(bo)
        conway_helper(bo)
        contract(bo)

        print("Board after iteration {}:".format(i+1))
        print_board(bo)

        if prev == bo:
            print("Board has reached its final state!")
            return

def init_board(points):
    sr = [point[0] for point in points]
    sc = [point[1] for point in points]
    rows = max(sr) - min(sr) + 1
    cols = max(sc) - min(sc) + 1

    bo = [['x' for col in range(cols)] for row in range(rows)]
    for point in points:
        r,c = point
        bo[r][c] = 'o'
    return bo

def expand(bo):
    new_rows = len(bo) + 2
    new_cols = len(bo[0]) + 2
    for i in range(new_rows):
        if i == 0:
            bo.insert(0, ['x'] * new_cols)
        elif i == new_rows - 1:
            bo.append(['x'] * new_cols)
        else:
            bo[i].insert(0, 'x')
            bo[i].append('x')

def conway_helper(bo):
    rows = len(bo)
    cols = len(bo[0])
    neighbors = [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)]
    for row in range(rows):
        for col in range(cols):
            live_neighbors = 0
            for neighbor in neighbors:
                r = row + neighbor[0]
                c = col + neighbor[1]
                if 0 <= r < rows and 0 <= c < cols and (bo[r][c] == 'o' or bo[r][c] == '-'):
                    live_neighbors += 1
            
            if bo[row][col] == 'o' and (live_neighbors < 2 or live_neighbors > 3):
                bo[row][col] = '-'
            elif bo[row][col] == 'x' and live_neighbors == 3:
                bo[row][col] = '+'
    
    for row in range(rows):
        for col in range(cols):
            if bo[row][col] == '+':
                bo[row][col] = 'o'
            elif bo[row][col] == '-':
                bo[row][col] = 'x'
    return bo

def contract(bo):
    try:
        while bo[0].count('x') == len(bo[0]):
            bo.pop(0)
    except:
        return
    
    try:
        while bo[-1].count('x') == len(bo[-1]):
            bo.pop()
    except:
        return
    
    try:
        l_col = [row[0] for row in bo]
        while l_col.count('x') == len(bo):
            for row in range(len(bo)):
                bo[row].pop(0)
            l_col = [row[0] for row in bo]
    except:
        return
    
    try:
        r_col = [row[-1] for row in bo]
        while r_col.count('x') == len(bo):
            for row in range(len(bo)):
                bo[row].pop()
            r_col = [row[-1] for row in bo]
    except:
        return

def print_board(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            print(bo[i][j], end=' ')
        print()
    print()

points = [(0,0),(1,1),(2,2),(3,3),(4,4),(5,5)]
k = 10
conway(points, k)