# The algorithm approach is stated as follows:
#
# First of all sort the array,
# Then find the longest divisible subsequence of the array.
# In order to find the longest divisible subsequence, we will follow the algorithm used to find the longest increasing
# subsequence discussed in the/** link to dp-42 **/.
# The distinguishing factor between longest increasing subsequence and longest divisible subsequence is that we used to
# insert the element if arr[i] > arr[prev] but here we will insert the element when arr[i] % arr[prev] == 0.
# At last return the hash array as the answer.
# time = O(n*n)
# Space = O(n)

def LDS(array):
    n = len(array)
    array = sorted(array)
    dp = [1] * n
    hash = [1] * n
    for ind in range(n):
        hash[ind] = ind
        for prev_ind in range(ind):
            if  array[ind]% array[prev_ind]  == 0 and 1 + dp[prev_ind] > dp[ind]:
                dp[ind] = 1 + dp[prev_ind]
                hash[ind] = prev_ind

    ans = last_ind = - 1
    for i in range(n):
        if ans < dp[i]:
            ans = dp[i]
            last_ind = i

    temp = [array[last_ind]]
    while hash[last_ind] != last_ind:
        last_ind = hash[last_ind]
        temp.append(array[last_ind])

    return temp[::-1]


array = [1,16,7,8,4]
print(LDS(array))
