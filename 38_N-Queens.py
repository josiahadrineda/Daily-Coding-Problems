def solveNQueens(n):
    res = []
    solveNQueensUtil(n, 0, [], res)
    
    for i in range(len(res)):
        for j in range(n):
            to_str = ['.'] * n
            to_str[res[i][j]] = 'Q'
            res[i][j] = ''.join(to_str)
    return res         

def solveNQueensUtil(n, row, cols, res):
    if row == n:
        res.append(cols.copy())
    else:
        for i in range(n):
            cols.append(i)
            if is_valid(cols):
                solveNQueensUtil(n, row+1, cols, res)
            cols.pop()

def is_valid(cols):
    row_ind = len(cols)-1
    for i in range(row_ind):
        diff = abs(cols[i]-cols[row_ind])
        if diff == 0 or diff == row_ind-i:
            return False
    return True

def print_sols(res):
    for sol in res:
        for row in sol:
            print(row)
        print()

#Driver code
for i in range(11):
    print(len(solveNQueens(i)))