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

def subsetSum(target, array, n):
    prev = [False for _ in range(target + 1)]

    prev[0] = True  # base case if target == 0
    if array[0] <= target:
        prev[array[0]] = True

    for ind in range(1, n):
        curr = [False for _ in range(target + 1)]
        curr[0] = True
        for tar in range(1, target + 1):
            notPick = prev[tar]
            pick = False
            if array[ind] <= tar:
                pick = prev[tar - array[ind]]
            curr[target] = pick or notPick
        prev = curr[:]
    return prev[target]


arr = [1, 2, 3, 4]
target = 4
print(subsetSum(target, arr, len(arr)))
