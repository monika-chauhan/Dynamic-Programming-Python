# A subsequence of a string is a list of characters of the string where some characters are deleted ( or not deleted at
# all) and they should be in the same order in the subsequence as in the original string.
# There are two possibility s1[i] == s2[i]: then move 1+ f(i-1,j-1) (1 added because one character matches)
# 2 possiblity :-> s1[i] != s2[j]: then max(f(i-1,j),f(i,j-1))
# Base case :
# if s1 completed and index become -1 then return 0
# if s2 completed and index become -1 then return 0
# time = O(n*m)
# time = O(n*m)

def longestCommonSubsequence(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(n+1):
        dp[i][0] = 0

    for j in range(m+1):
        dp[0][j] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = 0 + max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][m]


s1 = 'adebc'
s2 = 'dcadb'
print(longestCommonSubsequence(s1, s2))
