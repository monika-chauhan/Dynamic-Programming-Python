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

# time = O(n*n)
# space = O(n*n)

def minimumPathSumInTriangleMatrix(mat, n):
    dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
    for j in range(n):
        dp[n - 1][j] = mat[n - 1][j]  # last row copy into dp

    for i in range(n - 2, -1, -1):
        for j in range(i, -1, -1):
            down = mat[i][j] + dp[i + 1][j]
            diagonal = mat[i][j] + dp[i + 1][j + 1]

            dp[i][j] = min(down, diagonal)

    return dp[0][0]


triangle = [[1], [2, 3], [3, 6, 7], [8, 9, 6, 10]]
n = len(triangle)
print(minimumPathSumInTriangleMatrix(triangle, n))
