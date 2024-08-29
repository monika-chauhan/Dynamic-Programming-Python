# Given an array, ‘Arr’ of length ‘n’, count the number of longest increasing subsequences (LIS).
# after understanding the approach to finding the LIS, let us revisit the problem of counting the number of longest
# increasing subsequences of the array.
# Let us take a new array ct[ ] to calculate the count and initialize it to 1. Then ct[i] will be the count of the
# number of longest increasing subsequences where each LIS ends where arr[i] is the last element of the subsequence.
# Let us now understand the approach to get the values of the ct[ ] array, i.e to count the number of LIS.
# The initial example is given below and the dp[ ] and ct[ ] array are initialized to 1.
# we will iterate over the array and one by one see the final value of the dp[ ] means = LIS and
# ct[ ] array means the count of the LIS of the orignial aray that are possible of the length dp[i] with the element array[i]
# as its last element.
# At this stage, it is super important to have a crystal clear understanding of what dp[i] and ct[i]

# Approach:
# If we closely see the example we see two patterns for the nested loop conditions. We will always consider element at
# prev_index( say j) to place before element at index i only if arr[j] < arr[i]. Now, there arises two conditions:
# if( arr[j] < arr[i] && dp[j+1] > dp[i]), in this case we get a new LIS of greater length, therefore the number of LIS
# ending at arr[i], is the same as number of LIS ending at arr[j] as we simply append the element arr[j] to all those
# LIS. In simple terms, ct[i] = ct[j]. Try to dry run this example to understand: [1, 2, 3],
# if( arr[j] < arr[i] && dp[j+1]==dp[i]) in this case we get a new LIS of same length at which the ct[i] is originally
# holding the value for. Therefore the new ct[j] value will be the number of LIS that was given by its original value
# plus the number of LIS that ends at element arr[j] at length dp[j]. In simple terms, ct[i] = ct[i] + ct[j]. Try to
# dry run this example to understand: [1, 5, 6, 10].
# Based on these two conditions we can easily calculate the ct[ ]n array and return the ct[ ] value for the maximum
# value(s) of the dp[ ] array.


# time = O(n*n)
# space = O(n)


def countLIS(array):
    n = len(array)
    dp = [1] * n
    count = [1] * n
    maxi = 1
    for ind in range(n):
        for prev_ind in range(ind):
            if array[prev_ind] < array[ind] and 1 + dp[prev_ind] > dp[ind]:
                dp[ind] = 1 + dp[prev_ind]
                count[ind] = count[prev_ind]
            elif array[prev_ind] < array[ind] and dp[prev_ind] + 1 == dp[ind]:
                count[ind] += count[prev_ind]

        maxi = max(maxi, dp[ind])

    nos = 0
    for i in range(n):
        if dp[i] == maxi:
            nos += count[i]
    return nos


array = [1, 5, 4, 3, 2, 6, 7, 2]
print(countLIS(array))
