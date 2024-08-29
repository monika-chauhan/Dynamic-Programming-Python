# Given a number of stairs. Starting from the 0th stair we need to climb to the “Nth” stair.At a time we can climb
# either one or two steps. We need to return the total number of distinct ways to reach from 0th to Nth stair.

# time = o(n)
# space = O(n)
def climb_stair(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


print(climb_stair(4))
