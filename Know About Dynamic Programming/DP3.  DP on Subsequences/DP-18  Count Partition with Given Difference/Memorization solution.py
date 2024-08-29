# We are given an array ‘ARR’ with N positive integers and an integer D. We need to count the number of ways we can
# partition the given array into two subsets, S1 and S2 such that S1 – S2 = D and S1 is always greater than or
# equal to S2.
# conditions:
# 1. s1 > s2   -----equ(i)
# 2. S1 - S2 = D -----equ(ii)
# We observed that totalSum = S1 + S2 then S1 = totalSum - S2
# Put the value of s1 into equ no (ii) then
# totalSum - S2 - S2 = D => totalSum - 2*S2 = D
# totalSum - D = 2*S2
# S2 = (totalSum - D)//2 We can treat this as target and do the same thing in DP=17(count subset sum to K)
# Base Case:
# 1. totalSum - D not less than 0 :-> if totalSum - D < 0 : return False
# 2. totalSum - D % 2 is even only then only we can make two subsets
# constraints -> 0 <= array[i] <= n

# Time Complexity: O(N*K)
# Space Complexity: O(N*K) + O(N)
mod = int(1e9 + 7)


def countPartitionsUtil(ind, target, arr, dp):
    if ind == 0:
        if target == 0 and arr[0] == 0:
            return 2
        if target == 0 or target == arr[0]:
            return 1
        return 0

    if dp[ind][target] != -1:
        return dp[ind][target]

    notTaken = countPartitionsUtil(ind - 1, target, arr, dp)

    taken = 0
    if arr[ind] <= target:
        taken = countPartitionsUtil(ind - 1, target - arr[ind], arr, dp)

    dp[ind][target] = (notTaken + taken) % mod
    return dp[ind][target]


def countPartitions(d, arr):
    n = len(arr)
    totSum = sum(arr)

    # Checking for edge cases
    if totSum - d < 0:
        return 0
    if (totSum - d) % 2 == 1:
        return 0

    s2 = (totSum - d) // 2

    dp = [[-1 for j in range(s2 + 1)] for i in range(n)]
    return countPartitionsUtil(n - 1, s2, arr, dp)


arr = [5, 2, 6, 4]
n = len(arr)
d = 3
print(countPartitions(d, arr))
