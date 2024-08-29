# We are given an array ‘ARR’ with N positive integers and an integer K. We need to find the number of subsets
# whose sum is equal to K.
# Base Cases:
# If target == 0, it means that we have already found the subsequence from the previous steps, so we can return 1.
# If ind==0, it means we are at the first element, so we need to return arr[ind]==target. If the element is equal to
# the target we return 1 else we return 0.
# constraints : 0 < array[i] < n
# Time Complexity: O(N*K)
# Space Complexity: O(N*K)
def countSubsetSumToK(num, k, n):
    dp = [[-1 for _ in range(1 + k)] for _ in range(n)]
    dp = [[0] * (k + 1) for _ in range(n)]

    for i in range(n):  # Base case if target == 0
        dp[i][0] = 1

    if num[0] <= k:  # Base case if only one element is there and equal to k or less than
        dp[0][num[0]] = 1

    for ind in range(1, n):
        for target in range(1, k + 1):
            notTaken = dp[ind - 1][target]
            taken = 0
            if num[ind] <= target:
                taken = dp[ind - 1][target - num[ind]]
            dp[ind][target] = notTaken + taken
    return dp[n - 1][k]


array = [1, 2, 2, 3]
n = len(array)
k = 3
print(countSubsetSumToK(array, k, n))
