# Problem Statement: Given a row X cols binary matrix filled with 0’s and 1’s, find the largest rectangle containing
# only 1’s and return its area.
# Input: matrix = [[1,0,1,0,0],
#                  [1,0,1,1,1], --count 3 1's
#                  [1,1,1,1,1], -- count 3 1's
#                  [1,0,0,1,0]]
# Output: 6
# The algorithm steps are as follows:
#
# Declare a height array of size m(where m = no. of columns of the matrix).
# Now, we will run a loop to visit all the rows of the matrix.
# Now inside the loop, for each row, iterate over every column, and if a cell contains 1 we will increase the value of
# the column index by 1 in the height array i.e. height[col]++. But if the cell contains 0, we will set 0 for that
# column index in the height array.
# Once every cell gets visited, we will pass the height array i.e. the histogram array to the largestRectangleArea()
# function and store the maximum area for the row.
# Now, among all the areas calculated for all rows, we will keep the maximum one as our answer.

def largestRectangleArea(histogram):
    stack = []
    maxArea = 0
    n = len(histogram)
    for i in range(n+1):
        while len(stack) != 0 and i == n or histogram[stack[-1]] >= histogram[i]:
            height = histogram[stack[-1]]
            stack.pop()
            if len(stack) == 1:
                width = i
            else:
                width = i - stack[-1] - 1
            maxArea = max(maxArea, width * height)

        stack.append(i)
    return maxArea


def maximalAreaOfSubMatrixOFAll1(mat, n, m):
    maxArea = 0
    height = [0] * m
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                height[j] += 1
            else:
                height[j] = 0
        area = largestRectangleArea(height)
        maxArea = max(maxArea, area)
    return maxArea


matrix = [[1, 0, 1, 0, 0],
          [1, 0, 1, 1, 1],  # count 3 1's
          [1, 1, 1, 1, 1],  # count 3 1's
          [1, 0, 0, 1, 0]]
n = len(matrix)
m = len(matrix[0])
print(maximalAreaOfSubMatrixOFAll1(matrix, n, m))
