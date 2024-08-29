# We are given an array ‘ARR’ with N positive integers. We need to find if there is a subset in “ARR” with a sum equal
# to K. If there is, return true else return false.

# using Recursion approach if we find any subset with sum equal to target we return true
# Express the problem in terms of index
# f(ind, target):
# Base case-> 1. if target == 0:  True
# Base Case-> 2. if ind == 0: return a[0] == target
# Explore all the possibility of problem
# we have two choice 1.if array[ind] <= target: To pick the element and move ind - 1 and Target - a[ind]
# 2. Don't pick the element and move ind -1
# return pick or notPick => if either one is True return True

def subsetSum(ind, target, array):
    if target == 0: return True
    if ind == 0:
        return array[0] == target  # if it is True return True else return False
    notPick = subsetSum(ind - 1, target, array)
    pick = False
    if array[ind] <= target:
        pick = subsetSum(ind - 1, target - array[ind], array)
    return pick or notPick


arr = [1, 2, 3, 4]
target = 4
n = len(arr)
print(subsetSum(n - 1, target, arr))
