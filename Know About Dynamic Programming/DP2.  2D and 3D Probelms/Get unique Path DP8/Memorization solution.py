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

# time = O(n*m)
# Space = O(n*m)
def CountUniquPathInGrid(r, c):
    dp = [[-1] * (c + 1) for _ in range(r + 1)]
    if r == 0 and c == 0: return 1
    if r < 0 or c < 0: return 0
    if dp[r][c] != -1:
        return dp[r][c]

    up = CountUniquPathInGrid(r - 1, c)
    left = CountUniquPathInGrid(r, c - 1)
    dp[r][c] = up + left
    return dp[r][c]


m = 3
n = 2
print(CountUniquPathInGrid(m-1, n-1))
