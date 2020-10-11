def word_search(grid, word):
    if not grid or not word:
        return False

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if word_search_backtrack(grid, word, i, j, False, []):
                return True
    return False

def word_search_backtrack(grid, word, i, j, found_word, visited):
    if not word:
        found_word = True
    else:
        if is_valid(grid, word, i, j, visited):
            visited.append((i,j))
            for i,j in (i+1,j), (i-1,j), (i,j+1), (i,j-1):
                found_word = word_search_backtrack(grid, word[1:], i, j, found_word, visited)
    return found_word

def is_valid(grid, word, i, j, visited):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == word[0] and (i,j) not in visited

grid = [['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']]

assert word_search(grid, 'ABCCED')
assert word_search(grid, 'SEE')
assert not word_search(grid, 'ABCB')