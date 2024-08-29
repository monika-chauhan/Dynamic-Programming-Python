# A subsequence of an array is a list of elements of the array where some elements are deleted ( or not deleted at all)
# and they should be in the same order in the subsequence as in the original array.
# For example, for the array: [2,3,1] , the subsequences will be [{2},{3},{1},{2,3},{2,1},{3,1},{2,3,1}} but {3,2} is
# not a subsequence because its elements are not in the same order as the original array.
# What is the Longest Increasing Subsequence?
# The longest increasing subsequence is described as a subsequence of an array where:
# All elements of the subsequence are in increasing order.
# This subsequence itself is of the longest length possible.
# We will be taking f(ind, prev_ind)
# Base case = if ind == n: return 0
# explore all the possibility (pick if prev_ind == -1 and arr[ind] > arr[prev_ind] and update f(ind+1, ind),
# notPick f(ind+1, prev_ind)
# return max of pick and notPick

# time = O(2^n)
# space = O(n)

def LIS(ind, prev_ind, arr):
    n = len(arr)
    if ind == n: return 0
    notPick = 0 + LIS(ind + 1, prev_ind, arr)
    pick = 0
    if prev_ind == -1 or arr[ind] > arr[prev_ind]:
        pick = 1 + LIS(ind + 1, ind, arr)
    return max(pick, notPick)


array = [10, 9, 2, 5, 3, 7, 101, 18]
print(LIS(0, -1, array))
