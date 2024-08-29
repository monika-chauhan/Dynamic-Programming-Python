# A thief wants to rob a store. He is carrying a bag of capacity W. The store has ‘n’ items. Its weight is given by the
# ‘wt’ array and its value by the ‘val’ array. He can either include an item in its knapsack or exclude it but can’t
# partially have it as a fraction. We need to find the maximum value of items that the thief can steal.

# Base case
# If ind==0, it means we are at the first item, so in that case we will check whether this item’s weight is less than or
# equal to the current capacity W, if it is, we simply return its value (val[0]) else we return 0.
# Explore all the possibily pick and notpick
# return max(pick,notPick)

# Time = O(n*W)
# space = O(n*W) +O(n)

def knapsack(ind, wt, val, W, n):
    dp = [[-1 for _ in range(W + 1)] for _ in range(n)]
    if ind == 0:
        if wt[0] <= W:
            return val[0]
        return 0

    if dp[ind][W] != -1: return dp[ind][W]

    notPick = knapsack(ind - 1, wt, val, W, n)
    pick = float('-inf')
    if wt[ind] <= W:
        pick = val[ind] + knapsack(ind - 1, wt, val, W - wt[ind], n)
    dp[ind][W] = max(pick, notPick)
    return dp[ind][W]


wt = [1, 2, 4, 5]
val = [5, 4, 8, 6]
W = 5
n = len(wt)
print(knapsack(n - 1, wt, val, W, n))
