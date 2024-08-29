# In order to print the LIS, we maintain a separate array along with a dp array (say hash).
# Whenever we update our dp[i] value in the inner loop, we know that for index i, the previous index is prev_index.
# Therefore we simply store prev_index to hash[ i ]. In this way, we will have a way to trace back the LIS.
# Whenever we have computed the entire dp array and we find the maximum value in it. We store that maximum value’s index
# in a variable ( say last_index). Now with this last_index, and the hash array we can trace back the LIS elements.
# time = O(n*n)
# Space = O(n)
def printLIS(array, n):
    dp = [1] * n
    hash = [1] * n

    for i in range(n):
        hash[i] = i
        for prev_ind in range(i):
            if array[prev_ind] < array[i] and 1 + dp[prev_ind] > dp[i]:
                dp[i] = 1 + dp[prev_ind]
                hash[i] = prev_ind
    print(dp,hash)
    ans = -1
    last_ind = -1
    for i in range(n):
        if ans < dp[i]:
            ans = dp[i]
            last_ind = i

    temp = [array[last_ind]]
    while hash[last_ind] != last_ind:
        print(last_ind)
        last_ind = hash[last_ind]
        temp.append(array[last_ind])

    return temp[::-1], ans


array = [10, 9, 2, 5, 3, 7, 101, 18]
n = len(array)
print(printLIS(array, n))
