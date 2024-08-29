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

def subsetSum(array, target, n):
    dp = [[-1 for _ in range(target + 1)] for _ in range(n + 1)]
    for ind in range(n):
        dp[ind][0] = True
    if array[0] <= target:
        dp[0][array[0]] = True

    for ind in range(1, n):
        for tar in range(1, target + 1):
            notPick = dp[ind - 1][tar]
            pick = False
            if array[ind] <= target:
                pick = dp[ind - 1][tar - array[ind]]

            dp[ind][tar] = pick or notPick
    return dp[n - 1][target]


def canPartition(array, n):
    totSum = sum(array)
    if totSum % 2 == 1:
        return False
    else:
        return subsetSum(array, totSum // 2, n - 1)


arr = [2, 3, 3, 3, 4, 5]
n = len(arr)
print(canPartition(arr, n))
