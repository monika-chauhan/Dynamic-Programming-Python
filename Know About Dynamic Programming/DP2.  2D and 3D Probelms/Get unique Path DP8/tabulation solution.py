# Given two values M and N, which represent a matrix[M][N]. We need to find the total unique paths from the top-left
# cell (matrix[0][0]) to the rightmost cell (matrix[M-1][N-1]).
# M = row , N = col

# We will be doing a top-down recursion, i.e we will move from the cell[M-1][N-1] and try to find our way to the
# cell[0][0]. Therefore at every index, we will try to move up and towards the left.

# Base case
# When i=0 and j=0, that is we have reached the destination so we can count the current path that is going on, hence we
# return 1.
# When i<0 and j<0, it means that we have crossed the boundary of the matrix and we couldn’t find a right path, hence we
# return 0.

# Time = O(n*m)
# Space = O(n)
def CountUniquePathInGrid(r, c):
    dp = [[-1 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            # base condition
            if i == 0 and j == 0:
                dp[i][j] = 1
                continue
            up = left = 0
            if i > 0:
                up = dp[i - 1][j]
            if j > 0:
                left = dp[i][j - 1]

            dp[i][j] = up + left
    return dp[r - 1][c - 1]


row = 3
col = 2
print(CountUniquePathInGrid(row, col))
