# We are given an ‘N*M’ matrix. Every cell of the matrix has some chocolates on it, mat[i][j] gives us the number of
# chocolates. We have two friends ‘Alice’ and ‘Bob’. initially, Alice is standing on the cell(0,0) and Bob is standing
# on the cell(0, M-1).
# Both of them can move only to the cells below them in these three directions:to the bottom cell(↓),
# to the bottom-right cell(↘), or to the bottom-left cell(↙).
# When Alica and Bob visit a cell, they take all the chocolates from that cell with them. It can happen that they visit
# the same cell, in that case, the chocolates need to be considered only once.
# They cannot go out of the boundary of the given matrix, we need to return the maximum number of chocolates that Bob
# and Alice can together collect.
# function like f(i1,j1,i2,j2)  but We observe that the row is same for Alice and bob so function f(i,j1,j2)

# Base Case
# When i == N-1, it means we are at the last row,so we need to return from here. Now it can happen that at the last row,
# both Alice and Bob are at the same cell, in this condition
# we will return only chocolates collected by Alice, mat[i][j1](the chocolates cannot be doubly calculated),
# otherwise we return sum of chocolates collected by both, mat[i][j1] + mat[i][j2].

# Out of boundry case
# To move to the bottom-right cell(↘) or to the bottom-left cell(↙), it can happen that we may go out of bound as shown
# in the figure(below). So we need to handle it, we can return -1e9, whenever we go out of bound, in this way this path
# will not be selected by the calling function as we have to return the maximum chocolates.
# If j1 + di <0 or j1+di>=M or j2+dj<0 or j2+dj>=M  , then we return -1e9
# create front array = 2D (m*m) # store last row base on condition if j1 == j2 :
# create curr array => 2D(m*m)

# Time Complexity: O(N*M*M) * 9
# Space complexity : O(M*M)

def maximumChocolates(n, m, mat):
    front = [[0] * m for _ in range(m)]
    curr = [[0] * m for _ in range(m)]

    # Fill last row
    for j1 in range(m):
        for j2 in range(m):
            if j1 == j2:
                front[j1][j2] = mat[n - 1][j1]
            else:
                front[j1][j2] = mat[n - 1][j1] + mat[n - 1][j2]

    for i in range(n - 2, -1, -1):
        for j1 in range(m):
            for j2 in range(m):
                maxi = float('-inf')
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        ans = 0
                        if j1 == j2:
                            ans = mat[i][j1]
                        else:
                            ans = mat[i][j1] + mat[i][j2]

                        if (j1 + di < 0 or j1 + di >= m) or (j2 + dj < 0 or j2 + dj >= m):
                            ans += int(-1e9)
                        else:
                            ans += front[j1 + di][j2 + dj]
                        maxi = max(ans, maxi)

            curr[j1][j2] = maxi
        front = curr[:]
    return front[0][m-1]


matrix = [[2, 3, 1, 2], [3, 4, 2, 2], [5, 6, 3, 5]]

n = len(matrix)
m = len(matrix[0])

print(maximumChocolates(n, m, matrix))
