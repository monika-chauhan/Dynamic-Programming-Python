# A palindromic string is a string that is the same as its reverse. For example: “nitin” is a palindromic string.
# Now the question states that we are given a string, we need to find the minimum insertions that we can make in that
# string to make it a palindrome.
# ex-> s = 'abcaa' =>  Keep the palindrome LCS (aaa) and then insert as b and c the count = 2
# Minimum Insertion required = n(length of the string) – length of longest palindromic subsequence
# Algorithm
# We are given a string (say s), store its length as n.
# Find the length of the longest palindromic subsequence ( say k) as discussed in dp – 28
# Return n-k as answer.
# time = O(n*n)
# space = O(n*m)


def LCS(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(n + 1): dp[i][0] = 0
    for j in range(m + 1): dp[0][j] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][m]


def LongestPalindrome(s):
    t = s[::-1]
    return LCS(s, t)


def minInsertionReqToMakePalindrome(s):
    return len(s) - LongestPalindrome(s)


s = 'abcaa'
print(minInsertionReqToMakePalindrome(s))
