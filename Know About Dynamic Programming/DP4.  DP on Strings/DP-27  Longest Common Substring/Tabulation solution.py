# A substring of a string is a subsequence in which all the characters are consecutive. Given two strings, we need to
# find the longest common substring. We need to print the length of the longest common substring.
# ex-> s1 = 'abcjklp' s2 ='acjkp' => common => 'cjk'
# We have two conditions:
# if(S1[i-1] != S2[j-1]), the characters don’t match, therefore the consecutiveness of characters is broken.
# So we set the cell value (dp[i][j]) as 0.
# if(S1[i-1] == S2[j-1]), then the characters match and we simply set its value to 1+dp[i-1][j-1]. We have done so
# because dp[i-1][j-1] gives us the longest common substring till the last cell character
# (current strings -{matching character}). As the current cell’s character is matching we are adding 1 to the
# consecutive chain.

# Time Complexity: O(N*M)
# Reason: There are two nested loops
# Space Complexity: O(N*M)
def LongestCommonSubstring(s1,s2):
    n = len(s1)
    m = len(s2)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    ans = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                ans = max(ans,dp[i][j] )
            else:
                dp[i][j] = 0
    return ans

s1 = "abcjklp"
s2 = "acjkp"
print("The Length of Longest Common Substring is", LongestCommonSubstring(s1, s2))
