# We are given an array ‘ARR’ with N positive integers and an integer K. We need to find the number of subsets
# whose sum is equal to K.
# Base Cases:
# If target == 0, it means that we have already found the subsequence from the previous steps, so we can return 1.
# If ind==0, it means we are at the first element, so we need to return arr[ind]==target. If the element is equal to
# the target we return 1 else we return 0.
# constraints : 0 =< array[i] < n
# Time Complexity: O(N*K)
# Space Complexity: O(N*K) +O(n)

def countSubsetSumToK(ind, array, target, n):
    dp = [[-1 for _ in range(target + 1)] for _ in range(n)]
    if ind == 0:
        if array[0] == 0 and target == 0: return 2  # we have two choice beacause if num[0] = 0 and also sum == 0
        if array[0] == target and target == 0:
            return 1
        else:
            return 0

    if dp[ind][target] != -1: return dp[ind][target]

    notPick = countSubsetSumToK(ind - 1, array, target, n)
    pick = 0
    if array[ind] <= target:
        pick = countSubsetSumToK(ind - 1, array, target - array[ind], n)

    dp[ind][target] = pick + notPick
    return dp[ind][target]


nums = [0, 0, 1]
k = 1
n = len(nums)
print(countSubsetSumToK(n - 1, nums, k, n))
