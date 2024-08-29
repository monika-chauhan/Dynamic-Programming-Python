# Given an array of ‘N’  positive integers, we need to return the maximum sum of the subsequence such that no two
# elements of the subsequence are adjacent elements in the array.
# N = 3, a= [1,2,3] => pick a[0] , not pick a[1] , pick a[2] = > max(1+3,0) = 4
# N = 4 , a= [2,1,4,9] => pick a[0] , not pick a[1], not pick a[2] , pick a[3] => (2+9,0) = 11
# 2 condition:
# 1. If we pick an element then, pick = arr[ind] + f(ind-2). The reason we are doing f(ind-2) is because we have picked
# the current index element so we need to pick a non-adjacent element so we choose the index ‘ind-2’ instead of ‘ind-1’.
# 2. Next we need to ignore the current element in our subsequence. So nonPick= 0 + f(ind-1). As we don’t pick the
# current element, we can consider the adjacent element in the subsequence.

# time = O(n)
# space = O(1)

def maxSumNonAdj(a, n):
    prev0 = 0
    prev1 = a[0]
    for ind in range(1, n):
        pick = a[ind]
        if ind > 1:
            pick = a[ind] + prev0
        notPick = 0 + prev1
        curr = max(pick, notPick)
        prev0 = prev1
        prev1 = curr
    return prev1


array = [2, 1, 4, 9]
print(maxSumNonAdj(array, len(array)))
