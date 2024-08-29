# Given a number of stairs. Starting from the 0th stair we need to climb to the “Nth” stair. At a time we can climb
# either one or two steps. We need to return the total number of distinct ways to reach from 0th to Nth stair.

# in DP => dp[i] = dp[i-1]+dp[i-2] =>
# dp[i-1] = prev1
# dp[i-2] = prev2

# time = O(n)
# space = O(1)

def climb_stair(n):
    prev0 = 1
    prev1 = 1
    for i in range(2, n + 1):
        curr = prev0 + prev1
        prev0 = prev1
        prev1 = curr
    return prev1


print(climb_stair(3))
