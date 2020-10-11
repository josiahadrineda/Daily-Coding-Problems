def word_search(matrix, target):
    M, N = len(matrix), len(matrix[0])
    
    #Search by row
    for i in range(N):
        row = ''.join(matrix[i]).replace(' ', '')
        if target in row:
            return True

    #Search by column
    for i in range(M):
        col = ''.join([row[i] for row in matrix]).replace(' ', '')
        if target in col:
            return True

    return False

matrix = [['F','A','C','I'],
          ['O','B','Q','P'],
          ['A','N','O','B'],
          ['M','A','S','S']]
assert word_search(matrix, 'FOAM')
assert word_search(matrix, 'MASS')