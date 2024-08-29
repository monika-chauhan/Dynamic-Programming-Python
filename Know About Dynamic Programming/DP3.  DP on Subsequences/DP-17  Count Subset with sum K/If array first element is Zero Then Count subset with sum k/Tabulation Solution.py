# We are given an array ‘ARR’ with N positive integers and an integer K. We need to find the number of subsets
# whose sum is equal to K.
# Base Cases:
# If target == 0, it means that we have already found the subsequence from the previous steps, so we can return 1.
# If ind==0, it means we are at the first element, so we need to return arr[ind]==target. If the element is equal to
# the target we return 1 else we return 0.
# constraints : 0 =< array[i] < n
# Time Complexity: O(N*K)
# Space Complexity: O(N*K) +O(n)

def countSubsetSumToK(array, target, n):
    dp = [[-1 for _ in range(target + 1)] for _ in range(n)]

    if array[0] == 0:
        dp[0][0] = 2  # we have two choice beacause if num[0] = 0 and also sum == 0

    if array[0] == target:
        dp[0][target] = 1
    else:
        dp[0][target] = 0

    for ind in range(1, n):
        for tar in range(target + 1):
            notPick = dp[ind - 1][tar]
            pick = 0
            if array[ind] <= tar:
                pick = dp[ind - 1][tar - array[ind]]

            dp[ind][tar] = pick + notPick
    return dp[n - 1][target]


nums = [0, 0, 1]
k = 1
n = len(nums)
print(countSubsetSumToK(nums, k, n))
