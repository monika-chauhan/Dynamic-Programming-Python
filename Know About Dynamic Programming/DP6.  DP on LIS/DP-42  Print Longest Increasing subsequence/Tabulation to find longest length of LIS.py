# Algorithm approach:
# The algorithm approach can be stated as follows:
# Run an outer loop running from 0 to n-1. Every outer loop iteration will find the dp[i] value.
# Nest another loop inside it. For particular index i, this inner loop will help us to find the maximum value of
# dp[prev_index].
# Now inside the inner loop, we will first of all see that the element at the prev_index is smaller than the element at
# index i. If it is, we update dp[i] with the max(1+dp[prev_ind],dp[prev_index]).

# time = O(n*n)
# Space = O(n)

def LIS(array):
    n = len(array)
    dp = [1] * (n + 1)
    maxi = float('-inf')
    for ind in range(n):
        for prev_ind in range(ind):
            if array[ind] > array[prev_ind]:
                dp[ind] = max(dp[ind], 1 + dp[prev_ind])
                maxi = max(maxi, dp[ind])
    return maxi


array = [10, 9, 2, 5, 3, 7, 101, 18]
print(LIS(array))
