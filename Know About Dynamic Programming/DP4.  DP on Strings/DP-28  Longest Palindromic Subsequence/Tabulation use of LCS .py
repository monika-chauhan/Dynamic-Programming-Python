# A palindromic string is a string that is equal to its reverse. For example: “nitin” is a palindromic string. Now the
# question states to find the length of the longest palindromic subsequence of a string. It is that palindromic
# subsequence of the given string with the greatest length.
# We are given a string (say s), make a copy of it and store it( say string t).
# Reverse the original string s.
# Find the longest common subsequence

# Time Complexity: O(N*N)
# Reason: There are two nested loops
# Space Complexity: O(N*N)

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


s = "ccd"
print("The Length of Longest Palindromic Subsequence is ",LongestPalindrome(s))
