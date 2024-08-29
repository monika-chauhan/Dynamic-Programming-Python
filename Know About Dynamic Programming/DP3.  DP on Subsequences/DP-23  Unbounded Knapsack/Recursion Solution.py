# A thief wants to rob a store. He is carrying a bag of capacity W. The store has ‘n’ items of infinite supply.
# Its weight is given by the ‘wt’ array and its value by the ‘val’ array. He can either include an item in its knapsack
# or exclude it but can’t partially have it as a fraction. We need to find the maximum value of items that the thief can
# steal. He can take a single item any number of times he wants and put it in his knapsack.

# weight = [2,4,6] value = [5,11,13], capacity = 10
# pick 2 time (4 weight values i.e= 11) and 1 times (weight 2 value i.e 5 ) and sum up to steal max price values
# max => 11 + 11 + 5 = 27

#  Base Cases:
# If ind==0, it means we are at the first item. Now, in an unbounded knapsack we can pick an item any number of times
# we want. As there is only one item left, we will pick for W/wt[0] times because we ultimately want to maximize the
# value of items while respecting the constraint of weight of the knapsack. The value added will be the product of the
# number of items picked and value of the individual item. Therefore we return (W/wt[0]) * val[0].

# time = O(2^n)
# Space = O(n)

def unboundedKnapsack(ind, weight, value, W):
    if ind == 0:
        return W//weight[0] *  value[0]

    notPick = unboundedKnapsack(ind - 1, weight, value, W)
    pick = float('-inf')
    if weight[ind] <= W:
        pick = value[ind] + unboundedKnapsack(ind, weight, value, W - weight[ind])
    return max(pick, notPick)

wt = [2, 4, 6]
val = [5, 11, 13]
W = 10
n = len(wt)

print("The Maximum value of items, thief can steal is", unboundedKnapsack(n-1,wt,val,W))

