# Problem Statement: You are given n balloons, indexed from 0 to n – 1. Each balloon is painted with a number on it
# represented by an array. You are asked to burst all the balloons.
# If you burst the ith balloon, you will get arr[i – 1] * arr[i] * arr[i + 1] coins. If i – 1 or i + 1 goes out of the
# array’s bounds, then treat it as if there is a balloon with a 1 painted on it.
# Return the maximum coins you can collect by bursting the balloons wisely.

# Input: N = 4, array[] = {3, 1, 5, 8
# Output: 167
# Explanation:
# First, we will burst the second balloon with the value 1. Coins = 3*1*5 = 15.
# Second, we will burst the balloon with the value 5. Coins = 3*5*8 = 120.
# Third, we will burst the balloon with the value 3. Coins = 1*3*8 = 24.
# Fourth, we will burst the balloon with the value 8. Coins = 1*8*1 = 8.
# So, the total number of coins we can collect is 167. This is the maximum number of coins we can collect.

# Approach:
#
# The recursive algorithm steps are as follows:
#
# Append 1 to both ends of the given array.
# Convert the problem to a recursive function marked by two pointers i and j.
# Use a loop to check all possible combinations of balloons and get all possible total numbers of coins.
# Return the maximum number of coins we can get.
# Base case: If i > j, we will return 0.

# time =  O(2^n)
# Space = O(n)


def f(i, j, a, dp):
    if i > j: return 0
    if dp[i][j] != -1: return dp[i][j];
    maxi = float('-inf')
    for ind in range(i, j + 1):
        cost = a[i - 1] * a[ind] * a[j + 1] + f(i, ind - 1, a, dp) + f(ind + 1, j, a, dp);
        maxi = max(maxi, cost)
    return maxi


def maxBrustBalloonsPoint(balloons):
    n = len(balloons)
    balloons.insert(0, 1)
    balloons.append(1)
    dp = [[-1] * (n + 1)] * (n + 1)
    return f(1, n, balloons, dp)


a = [3, 1, 5, 8]
print(maxBrustBalloonsPoint(a))
