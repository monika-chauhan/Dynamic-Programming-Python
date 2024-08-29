# We are given an array Arr with N distinct coins and a target. We have an infinite supply of each coin denomination
# . We need to find the number of ways we sum up the coin values to give us the target.
# Each coin can be used any number of times.
# Ex = a = [1,2,3], target = 4
# {1,1,1,1} , { 1,1,2,}, {2,2},{1,3} Total ways = 4
# Base Case
# If ind==0, it means we are at the first item so we have only one coin denomination, therefore the following two
# cases can arise:
# case 1: T is divisible by arr[0]  (eg: arr[0] = 4 and T = 12)
# In such a case where the target is divisible by the coin element value, we will return 1 as we will be able to form
# the target.
# case 2: T is not divisible by arr[0] (eg: arr[0] = 4 and T = 7)
#  In all other cases, we will not be able to form the target, so we will return 0

def countWays(ind, coins, target):
    if ind == 0:
        return 1 if target % coins[0] == 0 else 0

    notPick = 0 + countWays(ind - 1, coins, target)
    pick = 0
    if coins[ind] <= target:
        pick = countWays(ind, coins, target - coins[ind])

    return pick + notPick


coins = [1, 2, 3]
target = 4
n = len(coins)
print(countWays(n - 1, coins, target))
