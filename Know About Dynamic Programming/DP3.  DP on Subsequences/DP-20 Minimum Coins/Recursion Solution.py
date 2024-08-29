# We are given a target sum of ‘X’ and ‘N’ distinct numbers denoting the coin denominations. We need to tell the minimum
# number of coins required to reach the target sum. We can pick a coin denomination for any number of times we want.

# Base Cases:
# If ind==0, it means we are at the first item, so in that case, the following cases can arise:
# arr[0] = 4 and T = 12
# In such a case where the target is divisible by the coin element, we will return T%arr[0].
# arr[0] =4 and T=1 , arr[0]=3 T=10
#  In all other cases, we will not be able to form a solution, so we will return a big number like 1e9
# Pick => Same Index only don't move (ind-1) and add 1 as well and NotPick

def minCoins(ind, coins, target):
    if ind == 0:
        if target % coins[0] == 0:
            return target // coins[0]
        else:
            return 1e9

    notPick = minCoins(ind - 1, coins, target)
    pick = 1e9
    if coins[ind] <= target:
        pick = 1 + minCoins(ind, coins, target - coins[ind])
    return min(pick, notPick)


array = [1, 2, 3]
k = 7
n = len(array)
print(minCoins(n - 1, array, k))
