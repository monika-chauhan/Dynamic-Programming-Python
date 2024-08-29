# We are given an array ‘ARR’ with N positive integers and an integer K. We need to find the number of subsets
# whose sum is equal to K.
# Base Cases:
# If target == 0, it means that we have already found the subsequence from the previous steps, so we can return 1.
# If ind==0, it means we are at the first element, so we need to return arr[ind]==target. If the element is equal to
# the target we return 1 else we return 0.
# constraints : 0 < array[i] < n

# Time Complexity: O(N*K)
# Space Complexity: O(K)
def countSubsetSumToK(num, k, n):
    prev = [0] *(1+k)
    prev[0] = 1  # Base case if target == 0
    if num[0] <= k:  # Base case if only one element is there and equal to k or less than
        prev[num[0]] = 1

    for ind in range(1, n):
        curr = [-1]*(1+k)
        curr[0] = 1
        for target in range(1, k + 1):
            notTaken = prev[target]
            taken = 0
            if num[ind] <= target:
                taken = prev[target - num[ind]]
            curr[target] = notTaken + taken
        prev = curr[:]
    return prev[k]


array = [1, 2, 2, 3]
n = len(array)
k = 3
print(countSubsetSumToK(array, k, n))
