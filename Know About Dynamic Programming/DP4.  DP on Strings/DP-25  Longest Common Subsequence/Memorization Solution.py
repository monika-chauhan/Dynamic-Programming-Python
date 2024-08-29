# A subsequence of a string is a list of characters of the string where some characters are deleted ( or not deleted at
# all) and they should be in the same order in the subsequence as in the original string.
# There are two possibility s1[i] == s2[i]: then move 1+ f(i-1,j-1) (1 added because one character matches)
# 2 possiblity :-> s1[i] != s2[j]: then max(f(i-1,j),f(i,j-1))
# Base case :
# if s1 completed and index become -1 then return 0
# if s2 completed and index become -1 then return 0
# time = O(n*m)
# time = O(n*m) + O(n*m)

def longestCommonSubsequence(i, j, s1, s2, n, m):
    dp = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
    if i < 0 or j < 0: return 0
    if dp[i][j] != -1: return dp[i][j]
    if s1[i] == s2[j]:
        dp[i][j] = 1 + longestCommonSubsequence(i - 1, j - 1, s1, s2, n, m)
    else:
        dp[i][j] = 0 + max(longestCommonSubsequence(i - 1, j, s1, s2, n, m),
                           longestCommonSubsequence(i, j - 1, s1, s2, n, m))
    return dp[i][j]


s1 = 'adebc'
s2 = 'dcadb'
n = len(s1)
m = len(s2)
print(longestCommonSubsequence(n - 1, m - 1, s1, s2, n, m))
