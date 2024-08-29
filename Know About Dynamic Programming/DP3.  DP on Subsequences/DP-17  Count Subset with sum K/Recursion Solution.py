# We are given an array ‘ARR’ with N positive integers and an integer K. We need to find the number of subsets
# whose sum is equal to K.
# Base Cases:
# If target == 0, it means that we have already found the subsequence from the previous steps, so we can return 1.
# If ind==0, it means we are at the first element, so we need to return arr[ind]==target. If the element is equal to
# the target we return 1 else we return 0.
# constraints : 0 < array[i] < n

def countSubsetSumToK(ind, array, target):
    if target == 0: return 1
    if ind == 0:
        return array[ind] == target

    notPick = countSubsetSumToK(ind - 1, array, target)
    pick = 0
    if array[ind] <= target:
        pick = countSubsetSumToK(ind - 1, array, target - array[ind])
    return pick + notPick


array = [1, 2, 2, 3]
n = len(array)
k = 3
print(countSubsetSumToK(n - 1, array, k))
