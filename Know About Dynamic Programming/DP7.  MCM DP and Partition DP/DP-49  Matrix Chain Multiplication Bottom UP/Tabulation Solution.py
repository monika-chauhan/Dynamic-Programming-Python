# Two matrices A1 and A2 of dimensions [p x q] and [r x s] can only be multiplied if and only if q=r.
# he total number of multiplications required to multiply A1 and A2 are: p*q*s

# Given a chain of matrices A1,…, An denoted by an array of size n+1, find out the minimum number of operations to
# multiply these n matrices.

# example: a = [10, 20, 30, 40, 50] => A1 = [10 X 20], A2 = [20 X 30] , A3 = [30 X 40], A4 = [40 X 50]

# Approach:
#
# As this problem of matrix multiplication solves one big problem ( minimum operations to get A1.A2….An) and the answer
# varies in the order the subproblems are being solved, we can identify this problem of pattern partition DP.

# Rules to solve the problem of partition DP:
# Start with the entire block/array and mark it with i,j. We need to find the value of f(i,j).
# Try all partitions.
# Run the best possible answer of the two partitions ( answer that comes after dividing the problem into two subproblems
# and solving them recursively).

# To summarize:
# Represent the entire array by two indexes i and j. In this question i =1 and j = n. We need to find f(i,j).
# Maintain a mini variable to get the minimum answer.
# Set a for loop to find the answer( variable k) from i to j-1,
# In every iteration find the answer, with the formula discussed above and compare it with the mini value.
# Return mini as the answer.

# time = O(n*n*n)
# Space = O(n*n) + O(n)

import sys


# Matrix Ai has dimension p[i-1] x p[i] for i = 1..n
def MatrixChainOrder(p, n):
    # For simplicity of the program, one extra row and one
    # extra column are allocated in m[][].  0th row and 0th
    # column of m[][] are not used
    m = [[0 for x in range(n)] for x in range(n)]

    # m[i, j] = Minimum number of scalar multiplications needed
    # to compute the matrix A[i]A[i + 1]...A[j] = A[i..j] where
    # dimension of A[i] is p[i-1] x p[i]

    # cost is zero when multiplying one matrix.
    for i in range(1, n):
        m[i][i] = 0

    # L is chain length.
    for L in range(2, n):
        for i in range(1, n - L + 1):
            j = i + L - 1
            m[i][j] = sys.maxsize
            for k in range(i, j):

                # q = cost / scalar multiplications
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q

    return m[1][n - 1]


# Driver program to test above function
array = [10, 20, 30, 40, 50]
size = len(array)

print("Minimum number of multiplications is " +
      str(MatrixChainOrder(array, size)))
# This Code is contributed by Bhavya Jain
