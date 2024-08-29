# A thief wants to rob a store. He is carrying a bag of capacity W. The store has ‘n’ items. Its weight is given by the
# ‘wt’ array and its value by the ‘val’ array. He can either include an item in its knapsack or exclude it but can’t
# partially have it as a fraction. We need to find the maximum value of items that the thief can steal.

# Base case
# If ind==0, it means we are at the first item, so in that case we will check whether this item’s weight is less than or
# equal to the current capacity W, if it is, we simply return its value (val[0]) else we return 0.
# Explore all the possiblity pick and notpick
# return max(pick,notPick)

# Time = O(n*W)
# space = O(n*W)

def knapsack(wt, val, W, n):
    dp = [[-1 for _ in range(W + 1)] for _ in range(n)]
    for i in range(wt[0], W + 1):
        dp[0][i] = val[0]

    for ind in range(1, n):
        for cap in range(W+1):
            notPick = 0 + dp[ind - 1][cap]
            pick = float('-inf')
            if wt[ind] <= cap:
                pick = val[ind] + dp[ind - 1][cap - wt[ind]]
            dp[ind][cap] = max(pick, notPick)
    return dp[n - 1][W]


wt = [1, 2, 4, 5]
val = [5, 4, 8, 6]
W = 5
n = len(wt)
print(knapsack(wt, val, W, n))
