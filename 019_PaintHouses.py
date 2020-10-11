"""
PREMISE:
A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the Nth row and Kth column represents the cost to build the Nth house with Kth color, return the minimum cost which achieves this goal.

AKA Select the min of elements in each row without selecting elements with the same index for any two adjacent rows.

LOGIC:
1) Copy first row to dp. Choosing any of the values in the first row is fair game as the first choice.
2) For every element in the next row, add its value to the min of the elements in the previous row except for the element directly above it (you cannot paint two adjacent houses the same color)
3) Repeat until i == N
4) Return the min of the elements in the last row (you've been adding them up until this point)
"""

def paint_houses(N: int, K: int, matrix: list) -> int:
    if not matrix:
        return 0
    elif len(matrix) == 1:
        return min(matrix[0])
    
    dp = [[0 for i in range(N)] for j in range(K)]
    dp[0] = matrix[0]

    for i in range(1, N):
        for j in range(K):
            prev = dp[i-1][:j] + dp[i-1][j+1:]
            dp[i][j] = matrix[i][j] + min(prev)
    
    return min(dp[N-1])

N,K = 4,4
matrix = [[1,1,2,2],
          [3,3,4,4],
          [5,5,6,6],
          [7,7,8,8]]
print(paint_houses(N, K, matrix))