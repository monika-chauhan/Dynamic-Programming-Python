# We are given an array ‘ARR’ with N positive integers and an integer D. We need to count the number of ways we can
# partition the given array into two subsets, S1 and S2 such that S1 – S2 = D and S1 is always greater than or
# equal to S2.
# conditions:
# 1. s1 > s2   -----equ(i)
# 2. S1 - S2 = D -----equ(ii)
# We observed that totalSum = S1 + S2 then S1 = totalSum - S2
# Put the value of s1 into equ no (ii) then
# totalSum - S2 - S2 = D => totalSum - 2*S2 = D
# totalSum - D = 2*S2
# S2 = (totalSum - D)//2 We can treat this as target and do the same thing in DP=17(count subset sum to K)
# Base Case:
# 1. totalSum - D not less than 0 :-> if totalSum - D < 0 : return False
# 2. totalSum - D % 2 is even only then only we can make two subsets
# constraints -> 0 <= array[i] <= n
def countSubsetSumToK(ind, array, target, n):
    if ind == 0:
        if array[0] == 0 and target == 0: return 2
        if array[0] == target or target == 0:
            return 1
        else:
            return 0

    notPick = countSubsetSumToK(ind - 1, array, target, n)
    pick = 0
    if array[ind] <= target:
        pick = countSubsetSumToK(ind - 1, array, target - array[ind], n)
    return pick + notPick


def countPartitions(array, d, n):
    totalSum = sum(array)
    if (totalSum - d) < 0 or (totalSum - d) % 2 == 1:
        return 0
    return countSubsetSumToK(n - 1, array, (totalSum - d) // 2, n)


arr = [5, 2, 6, 4]
n = len(arr)
d = 3
print(countPartitions(arr, d, n))
