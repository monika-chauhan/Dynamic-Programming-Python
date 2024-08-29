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

def subsetSum(target, array, n):
    prev = [False] * (target + 1)
    prev[0] = True
    if array[0] <= target:
        prev[array[0]] = True

    for ind in range(1, n):
        curr = [False] * (target + 1)
        curr[0] = True
        for tar in range(target + 1):
            notPick = prev[tar]
            pick = False
            if array[ind] <= tar:
                pick = prev[tar - array[ind]]
            curr[tar] = pick or notPick

        prev = curr[:]

    return prev[n - 1]


def canPartition(array, n):
    totSum = sum(array)
    if totSum % 2 == 0:
        return subsetSum(totSum // 2, array, n)
    else:
        return False


arr = [2, 3, 3, 3, 4, 5]
n = len(arr)
print(canPartition(arr, n))
