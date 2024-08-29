# We are given a target sum of ‘X’ and ‘N’ distinct numbers denoting the coin denominations. We need to tell the minimum
# number of coins required to reach the target sum. We can pick a coin denomination for any number of times we want.

# Base Cases:
# If ind==0, it means we are at the first item, so in that case, the following cases can arise:
# arr[0] = 4 and T = 12
# In such a case where the target is divisible by the coin element, we will return T%arr[0].
# arr[0] =4 and T=1 , arr[0]=3 T=10
#  In all other cases, we will not be able to form a solution, so we will return a big number like 1e9
# Pick => Same Index only don't move (ind-1) and add 1 as well and NotPick

def minCoins(coins, target, n):
    prev = [0]*(target+1)
    curr = [0]*(target+1)
    for i in range(target+1):
        if i % coins[0] == 0:
            prev[i] = i//coins[0]
        else:
            prev[i] = 1e9

    for ind in range(1,n):
        for tar in range(target+1):
            notPick = prev[tar]
            pick = 1e9
            if coins[ind] <= tar:
                pick = 1 + curr[tar - coins[ind]]
            curr[tar] = min(pick, notPick)
        prev = curr[:]
    return prev[target]


array = [1, 2, 3]
k = 7
n = len(array)
print(minCoins(array, k, n))
