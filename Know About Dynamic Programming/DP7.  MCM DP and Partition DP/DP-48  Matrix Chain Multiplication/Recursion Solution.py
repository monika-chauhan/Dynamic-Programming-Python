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

def MCM(start, end, array):
    if start == end: return 0
    mini = float('inf')
    for k in range(start, end):
        ans = array[start - 1] * array[k] * array[end] + MCM(start, k, array) + MCM(k + 1, end, array)
        mini = min(mini, ans)
    return mini


array = [10, 20, 30, 40, 50]
n = len(array)
start = 1
end = n - 1
print(MCM(start, end, array))
