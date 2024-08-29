# We are given an array ‘ARR’ with N positive integers. We need to find if we can partition the array into two subsets
# such that the sum of elements of each subset is equal to the other.
# array = [2,3,3,3,4,5]
# subset1 = [2,3,5] => s1 = 10 , Subset2 = [3,3,4] => s2 = 10
# if totalSum is even then only we can partition equal else not able to partition
# we can make , target = totalSum // 2 => s1 = s2 = totalSum//2
# Then do the same SubsetSum DP-14 code
# Base Cases:
# If target == 0, it means that we have already found the subsequence from the previous steps, so we can return true.
# If ind==0, it means we are at the first element, so we need to return arr[ind]==target. If the element is equal to
# the target we return true else false.

def subsetSum(ind, array, target):
    if target == 0: return True
    if ind == 0:
        return array[ind] == target

    notPick = subsetSum(ind - 1, array, target)
    pick = False
    if array[ind] <= target:
        pick = subsetSum(ind - 1, array, target - array[ind])

    return pick or notPick


def canPartition(array, n):
    totSum = sum(array)
    if totSum % 2 == 0:
        return subsetSum(n - 1, array, totSum // 2)
    else:
        return False


arr = [2, 3, 3, 4, 5]
n = len(arr)
print(canPartition(arr, n))

