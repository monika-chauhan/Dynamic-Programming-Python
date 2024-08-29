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

# time = O(n*w)
# Space = O(W)

def unboundedKnapsack(weight, value, W, n):
    prev = [0] * (W+1)
    curr = [0]*(W+1)
    for i in range(W + 1):
        prev[i] = i // weight[0] * value[0]

    for ind in range(1, n):
        for cap in range(W + 1):
            notPick = prev[cap]
            pick = float('-inf')
            if weight[ind] <= cap:
                pick = value[ind] + curr[cap - weight[ind]]
            curr[cap] = max(pick, notPick)
        prev = curr[:]
    return prev[W]


wt = [2, 4, 6]
val = [5, 11, 13]
W = 10
n = len(wt)

print("The Maximum value of items, thief can steal is", unboundedKnapsack(wt, val, W, n))
