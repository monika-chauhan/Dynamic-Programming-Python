# We are given an “N*M” Maze. The maze contains some obstacles. A cell is ‘blockage’ in the maze if its value is -1. 0
# represents non-blockage. There is no path possible through a blocked cell.
#
# We need to count the total number of unique paths from the top-left corner of the maze to the bottom-right corner. At
# every cell, we can move either down or towards the right.

# We will be doing a top-down recursion, i.e we will move from the cell[M-1][N-1] and try to find our way to the
# cell[0][0]. Therefore at every index, we will try to move up and towards the left.

# Base Case:
# There will be three base cases:
# 1. When i>0 and j>0 and mat[i][j] = -1, it means that the current cell is an obstacle, so we can’t find a path from
# here. Therefore, we return 0.
# 2. When i=0 and j=0, that is we have reached the destination so we can count the current path that is going on, hence
# we return 1.
# 3.When i<0 and j<0, it means that we have crossed the boundary of the matrix and we couldn’t find a right path, hence
# we return 0.

def CountPathInGridbyNonBlockCell(m, n, mat):
    # Base case
    if m > 0 and n > 0 and mat[m][n] == -1: return 0
    if m < 0 or n < 0: return 0  # out of boundry
    if m == 0 and n == 0: return 1

    up = CountPathInGridbyNonBlockCell(m - 1, n, mat)
    left = CountPathInGridbyNonBlockCell(m, n - 1, mat)
    return up + left


maze = [[0, 0, 0], [0, -1, 0], [0, 0, 0]]
m = len(maze)
n = len(maze[0])
print(CountPathInGridbyNonBlockCell(m-1, n-1, maze))
