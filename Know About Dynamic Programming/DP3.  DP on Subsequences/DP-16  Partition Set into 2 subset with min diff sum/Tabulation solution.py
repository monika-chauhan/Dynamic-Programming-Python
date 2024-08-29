# We are given an array ‘ARR’ with N positive integers. We need to partition the array into two subsets such that the
# absolute difference of the sum of elements of the subsets is minimum.
# We need to return only the minimum absolute difference of the sum of elements of the two partitions.

# Base Cases:
# If target == 0, it means that we have already found the subsequence from the previous steps, so we can return true.
# If ind==0, it means we are at the first element, so we need to return arr[ind]==target. If the element is equal to
# the target we return true else false.

# Time Complexity: O(N*totSum) +O(N) +O(N)
# Space Complexity: O(N*totSum)

def minSubsetSumDifference(array, n):
    totSum = sum(array)
    dp = [[False for _ in range(1 + totSum)] for _ in range(1 + n)]
    for i in range(n):
        dp[i][0] = True

    if array[0] <= totSum:
        dp[0][totSum] = True

    for ind in range(1, n):
        for target in range(1, totSum + 1):
            notPick = dp[ind - 1][target]
            pick = False
            if array[ind] <= target:
                pick = dp[ind - 1][target - array[ind]]
            dp[ind][target] = pick or notPick

    mini = 1e9
    for i in range(totSum // 2 + 1):
        if dp[n - 1][i]:  # is equal to True
            diff = abs(i - (totSum - i))
            mini = min(mini, diff)
    return mini


arr = [1, 2, 3, 4]
n = len(arr)
print("The minimum absolute difference is:", minSubsetSumDifference(arr, n))
