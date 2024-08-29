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

mod = int(1e9 + 7)


def countPartitionsUtil(ind, target, arr, ):
    dp = [[0] * (target + 1) for _ in range(n)]

    if arr[0] == 0:
        dp[0][0] = 2  # 2 cases - pick and not pick
    else:
        dp[0][0] = 1

    if arr[0] != 0 or arr[0] <= target:
        dp[0][arr[0]] = 1  # 1 case - pick

    for ind in range(1, n):
        for tar in range(target + 1):
            notTaken = dp[ind - 1][tar]

            taken = 0
            if arr[ind] <= tar:
                taken = dp[ind - 1][tar - arr[ind]]

            dp[ind][tar] = (notTaken + taken) % mod
    return dp[n - 1][target]


def countPartitions(d, arr):
    n = len(arr)
    totSum = sum(arr)

    # Checking for edge cases
    if totSum - d < 0 or (totSum - d) % 2 == 1:
        return 0
    s2 = (totSum - d) // 2

    return countPartitionsUtil(n - 1, s2, arr)


arr = [5, 2, 6, 4]
n = len(arr)
d = 3
print(countPartitions(d, arr))
