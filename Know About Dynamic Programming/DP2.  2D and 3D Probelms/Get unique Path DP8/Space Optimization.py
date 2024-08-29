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

# Time = O(m*n)
# Space = O(n)

def countUniquePathIngrid(m,n):
    prev = [0] * n
    for i in range(m):
        temp = [0] * n
        for j in range(n):
            if i == 0 and j == 0:
                temp[j] = 1
                continue

            up = 0
            left = 0

            if i > 0:
                up = prev[j]
            if j > 0:
                left = temp[j - 1]

            temp[j] = up + left
        prev = temp

    return prev[n - 1]

row = 3
col = 2
print(countUniquePathIngrid(row, col))