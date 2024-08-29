# Approach:
#
# The recursive algorithm steps are as follows:
#
# Convert the problem to a recursive function marked by the pointer i.
# Use a loop to check all possible partitions of the string and calculate the number of partitions.
# Return the minimum number of partitions counted.
# Base case: When the index i will be equal to the size of the string(i.e. i == n), we can say there are no more
# characters left to be partitioned. So, this is the base case and in this case, the function will return 0.

# Input: s = “bababcbadcede”
# Output: 4
# Explanation: If we do 4 partitions in the following way,
# each substring of the partition will be a palindrome.
# bab | abcba | d | c | ede
# iterate loop j > 0,n => cost = 1 + f(j+1,n)
#  our actual answer will be (number of partitions returned by the function – 1).

# time = O(n*n)
# Space = O(n)
def isPalindrome(i, j, s):
    while i < j:
        if s[i] != s[j]: return False
        i += 1
        j -= 1
    return True


def palinPartitionReq(s):
    n = len(s)
    dp = [0] * (n + 1)
    dp[n] = 0
    for i in range(n - 1, -1, -1):
        minCost = float('inf')
        for j in range(i, n):
            if isPalindrome(i, j, s):
                cost = 1 + dp[j + 1]
                minCost = min(minCost, cost)
        dp[i] = minCost
    return dp[0] - 1


s = "BABABCBADCEDE"
print(palinPartitionReq(s))
