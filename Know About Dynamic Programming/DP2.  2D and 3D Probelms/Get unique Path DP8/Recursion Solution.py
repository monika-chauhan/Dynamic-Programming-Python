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

def CountUniquePathInGrid(r, c):
    if r == 0 and c == 0: return 1
    if r < 0 or c < 0: return 0  # either one goes below 0
    up = CountUniquePathInGrid(r - 1, c)  # from last cell [2,2] we move up toward [1][2] cell
    left = CountUniquePathInGrid(r, c - 1)  # from last cell [2,2] we move left toward [2][1] cell
    return up + left  # total count of path


m = 3
n = 2
print(CountUniquePathInGrid(m - 1, n - 1))
