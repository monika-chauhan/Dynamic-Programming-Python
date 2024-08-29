# Problem Statement: Given an integer array arr, partition the array into (contiguous) subarrays of length at
# most k. After partitioning, each subarray has its values changed to become the maximum value of that subarray.
# Return the largest sum of the given array after partitioning.
# Input: arr = [1,15,7,9,2,5,10], k = 3
# Output: 84
# Explanation: The partition will be the following to get the largest sum:
#  [1, 15, 7 | 9 | 2, 5, 10].
# After replacing the elements of each subarray with its maximum, the array will look like this:[15,15,15,9,10,10,10]
# and the sum will be 84.
# Note: It may happen that the limit ind+k-1 exceeds the length of the array. That is why we will take the limit of j as
# min(n, ind+k-1) where n = size of the array. This will avoid the runtime error.
# Base case: When the value of ind becomes equal to n(n = size of the array), we can say there are no elements left to
# be considered. So, when (ind == n) the function will return 0.
# Approach:
# The recursive algorithm steps are as follows:
# Convert the problem to a recursive function marked by the pointer ind.
# Use a loop to check all possible partitions of the array and calculate the maximum sum we can achieve.
# Return the maximum possible sum.

def f(ind, array, k):
    n = len(array)
    Len = 0
    maxEle = float('-inf')
    maxAns = float('-inf')
    if ind == n:
        return 0
    for j in range(ind, min(ind + k, n)):
        Len += 1
        maxEle = max(maxEle, array[j])
        sum = Len * maxEle + f(j + 1, array, k)
        maxAns = max(maxAns, sum)
    return maxAns


def PartitionMaxSumArr(array, k):
    return f(0, array, k)


array = [1, 15, 7, 9, 2, 5, 10]
k = 3
print(PartitionMaxSumArr(array, k))
