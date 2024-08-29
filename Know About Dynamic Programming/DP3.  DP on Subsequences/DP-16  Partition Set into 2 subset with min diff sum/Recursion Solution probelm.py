# We are given an array ‘ARR’ with N positive integers. We need to partition the array into two subsets such that the
# absolute difference of the sum of elements of the subsets is minimum.
# We need to return only the minimum absolute difference of the sum of elements of the two partitions.

# Base Cases:
# If target == 0, it means that we have already found the subsequence from the previous steps, so we can return true.
# If ind==0, it means we are at the first element, so we need to return arr[ind]==target. If the element is equal to
# the target we return true else false.

def subsetSum(ind, target, array):
    if target == 0: return True
    if ind == 0: return array[0] == target
    notPick = subsetSum(ind - 1, target, array)
    pick = False
    if array[ind] <= target:
        pick = subsetSum(ind - 1, target - array[ind], array)
    return pick or notPick


def minSubsetSumDifference(array,n):
    totSum = sum(array)
    mini = 1e9

    for i in range(totSum//2+1):
        if subsetSum(n - 1, i, array):
            diff = abs(i - (totSum-i))
            mini = min(mini,diff)
    return mini

arr = [1, 2, 3, 4]
n = len(arr)
print("The minimum absolute difference is:", minSubsetSumDifference(arr,n))