# We are given an “N*M” matrix of integers. We need to find a path from the top-left corner to the bottom-right corner
# of the matrix, such that there is a minimum cost past that we select.
# At every cell, we can move in only two directions: right and bottom. The cost of a path is given as the sum of values
# of cells of the given matrix.

# We will be doing a top-down recursion, i.e we will move from the cell[M-1][N-1] and try to find our way to the
# cell[0][0]. Therefore at every index, we will try to move up and towards the left.

# Base Case:
# There will be three base cases:
# When i=0 and j=0, that is we have reached the destination so we can add to path the current cell value, hence we
# return mat[0][0].
# When i<0 or j<0, it means that we have crossed the boundary of the matrix and we don’t want to find a path from here,
# so we return a very large number( say, 1e9) so that this path is rejected by the calling function.

# As we are writing a top-down recursion, at every index we have two choices, one to go up(↑) and the other go left(←).
# To go upwards, we will reduce i by 1, and move towards left we will reduce j by 1.
#
# Now when we get our answer for the recursive call (f(i-1,j) or f(i,j-1)), we need to also add the current cell value
# to it as we have to include it too for the current path sum.
# time = O(m*n)
# Space = O(m*n)

def minPathSumInGrid(m, n, mat):
    dp = [[-1 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = mat[i][j]
                continue
            else:
                up = mat[i][j]
                if i > 0:
                    up += dp[i - 1][j]
                else:
                    up += 1e9

                left = mat[i][j]
                if j > 0:
                    left += dp[i][j - 1]
                else:
                    left += 1e9
                dp[i][j] = min(up, left)

    return dp[m-1][n-1]


grid = [[5, 9, 6], [11, 5, 2]]
m = len(grid)
n = len(grid[0])
print(minPathSumInGrid(m , n , grid))
