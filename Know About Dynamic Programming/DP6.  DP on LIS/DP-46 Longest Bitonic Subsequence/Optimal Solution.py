# Given an array, ‘Arr’ of length ‘n’, find the longest bitonic subsequence
# Problem Statement:
# Let us first understand what a bitonic subsequence means.
# A bitonic subsequence is a subsequence of an array in which the elements can be any of these three:
# First, increase till a point and then decrease.
# Goes on increasing (Longest increasing subsequence)
# Goes on decreasing (Longest decreasing subsequence)
# a subsequence having the elements in either increasing or decreasing order only also counts as a bitonic subsequence
# We need to return the length of the longest bitonic subsequence as our answer.

# Approach:
# The algorithm approach is stated as follows:
# Using the approach of the article Printing Longest Increasing subsequence, find the dp1[ ] array, where dp1[i] gives
# us the length of the LIS from index 0 to index i.
# Modifying the approach slightly, find the dp2[ ] array, where dp2[i] gives us the length of the LIS from index n-1 to
# index i. To find this opposite direction LIS simply reverses the direction of variables in the nested loops .
# At last return the answer (the length of the longest bitonic subsequence) as the maximum value of dp1[i] – dp2[i] -1.


# time = O(n*n)
# Space = O(n)

def LongestBitonicSeq(array):
    n = len(array)
    dp1 = [1] * n
    dp2 = [1] * n

    for ind in range(n):
        for prev_ind in range(ind):
            if array[prev_ind] < array[ind]:
                dp1[ind] = max(dp1[ind], 1 + dp1[prev_ind])

    for ind in range(n - 1, -1, -1):
        for prev_ind in range(n - 1, ind, -1):
            if array[prev_ind] < array[ind]:
                dp2[ind] = max(dp2[ind], 1 + dp2[prev_ind])

    maxi = -1
    for i in range(n):
        maxi = max(maxi, dp1[i] + dp2[i] - 1)
    return maxi


array = [1, 11, 2, 10, 4, 5, 2, 1]
print(LongestBitonicSeq(array))
