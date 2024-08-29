# We are given a Triangular matrix. We need to find the minimum path sum from the first row to the last row.

# At every cell we can move in only two directions: either to the bottom cell (↓) or to the bottom-right cell(↘)

# Base Case:
# There will be a single base case:
# When i == N-1, that is when we have reached the last row, so the min path from that cell to the last row will be the
# value of that cell itself, hence we return mat[i][j].

# At every index we have two choices, one to go to the bottom cell(↓) other to the bottom-right cell(↘). To go to the
# bottom, we will increase i by 1 i.e a[i][j] + fun(i+1,j), and to move towards the bottom-right we will increase both i and j
# by 1 i.e. a[i][j] + fun(i+1,j+1)

# Ans is min a[i][j] + fun(i+1,j),a[i][j] + fun(i+1,j+1))

def minimumPathSumInTriangleMatrix(i, j, mat, n):
    if i == n - 1:
        return mat[i][j]
    down = mat[i][j] + minimumPathSumInTriangleMatrix(i + 1, j, mat, n)
    diagonal = mat[i][j] + minimumPathSumInTriangleMatrix(i + 1, j + 1, mat, n)
    return min(down, diagonal)


triangle = [[1], [2, 3], [3, 6, 7], [8, 9, 6, 10]]
n = len(triangle)
print(minimumPathSumInTriangleMatrix(0, 0, triangle, n))
