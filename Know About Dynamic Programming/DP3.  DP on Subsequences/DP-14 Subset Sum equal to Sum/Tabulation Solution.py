# We are given an array ‘ARR’ with N positive integers. We need to find if there is a subset in “ARR” with a sum equal
# to K. If there is, return true else return false.

# using Recursion approach if we find any subset with sum equal to target we return true
# Express the problem in terms of index
# f(ind, target):
# Base case-> 1. if target == 0:  True
# Base Case-> 2. if ind == 0: return a[0] == target
# Explore all the possibility of problem
# we have two choice 1.if array[ind] <= target: To pick the element and move ind - 1 and Target - a[ind]
# 2. Don't pick the element and move ind -1
# return pick or notPick => if either one is True return True

def subsetSum(target, array, n):
    dp = [[-1 for _ in range(target+1)] for _ in range(n)]
    for ind in range(n):
        dp[ind][0] = True

    if array[0] <= target:
        dp[0][array[0]] = True

    for ind in range(1,n):
        for tar in range(1,target+1):
            notPick = dp[ind-1][tar]
            pick = False
            if array[ind] <= target:
                pick = dp[ind-1][tar-array[ind]]
            dp[ind][tar] = pick or notPick
    return dp[n-1][tar]


arr = [1, 2, 3, 4]
target = 4
n = len(arr)
print(subsetSum(target, arr, len(arr)))
