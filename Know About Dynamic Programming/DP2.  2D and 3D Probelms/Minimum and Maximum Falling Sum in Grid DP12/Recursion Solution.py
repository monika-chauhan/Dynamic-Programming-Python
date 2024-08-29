# We are given an ‘N*M’ matrix. We need to find the maximum path sum from any cell of the first row to any cell of the
# last row.
# At every cell we can move in three directions: to the bottom cell (↓), to the bottom-right cell(↘),
# or to the bottom-left cell(↙).
# We have a top row and a bottom row, we will be writing a recursion in the direction of the last row to the first row.
# For the last row, i=N-1 therefore we need to find four different answers:
# f(N-1,0), f(N-1,1), f(N-1,2), f(N-1,3)

# Base Case:
# When i == 0, it means we are at the first row, so the min path from that cell to the first will be the value of
# that cell itself, hence we return mat[0][j].

# To move to the top-left cell(↖) or to the top-right cell(↗), it can happen that we may go out of bound as shown in the
# figure(below). So we need to handle it, we can return -1e9, whenever we go out of bound, in this way this path will
# not be selected by the calling function as we have to return the maximum path.
# If j<0 or j>=M , then we return -1e9

def getMaxPathSumUntill(i, j, m, mat):  # start from last row to first row
    if j < 0 or j >= m:  # out of boundary  (left for first col ,right for the last col)
        return -1e9
    if i == 0:
        return mat[0][j]
    up = mat[i][j] + getMaxPathSumUntill(i - 1, j, m, mat)  # from last row to up (row will decrease)
    diagonal_left = mat[i][j] + getMaxPathSumUntill(i - 1, j - 1, m,
                                                    mat)  # from last row to up left(row and col both decrease)
    diagonal_right = mat[i][j] + getMaxPathSumUntill(i - 1, j + 1, m,
                                                     mat)  # from last row to up right(row decrease but col increse)
    return max(up, diagonal_left, diagonal_right)


def getMaxPathSum(matrix):
    n = len(matrix)
    m = len(matrix[0])
    maxi = float('-inf')
    for j in range(m):
        ans = getMaxPathSumUntill(n - 1, j, m, matrix)
        maxi = max(maxi, ans)
    return maxi


matrix = [[1, 2, 10, 4], [100, 3, 2, 1], [1, 1, 20, 2], [1, 2, 2, 1]]
print(getMaxPathSum(matrix))