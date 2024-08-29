# A thief wants to rob a store. He is carrying a bag of capacity W. The store has ‘n’ items. Its weight is given by the
# ‘wt’ array and its value by the ‘val’ array. He can either include an item in its knapsack or exclude it but can’t
# partially have it as a fraction. We need to find the maximum value of items that the thief can steal.

# Base case
# If ind==0, it means we are at the first item, so in that case we will check whether this item’s weight is less than or
# equal to the current capacity W, if it is, we simply return its value (val[0]) else we return 0.
# Explore all the possiblity pick and notpick
# return max(pick,notPick)

# Time = O(n*W)
# space = O(W)

def knapsack(wt, val, W, n):
    prev = [0] * (W + 1)
    curr = [0] * (W + 1)
    for i in range(wt[0], W + 1):
        prev[i] = val[0]

    for ind in range(1, n):
        for cap in range(W + 1):
            notPick = 0 + prev[cap]
            pick = float('-inf')
            if wt[ind] <= cap:
                pick = val[ind] + prev[cap - wt[ind]]
            curr[cap] = max(pick, notPick)
        prev = curr[:]
    return prev[W]


wt = [1, 2, 4, 5]
val = [5, 4, 8, 6]
W = 5
n = len(wt)
print(knapsack(wt, val, W, n))
