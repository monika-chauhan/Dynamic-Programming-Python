#  print the length of the longest common subsequence of two strings.

# We will continue from where we left in the article DP-25. There in the tabulation approach, we declared a dp array
# and dp[n][m] will have the length of the longest common subsequence., i.e dp[n][m] = 3.
# Now, with help of two nested loops, if we print the dp array, it will look like this:

# Now, let us see what were the conditions that we used while forming the dp array:
# if(S1[i-1] == S2[j-1]), then return 1 + dp[i-1][j-1]
# if(S1[i-1] != S2[j-1]) , then return 0 + max(dp[i-1][j],dp[i][j-1])

# Time Complexity: O(N*M)
# Reason: There are two nested loops
# Space Complexity: O(N*M)

def LCS(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(n + 1):
        dp[i][0] = 0

    for j in range(m + 1):
        dp[0][j] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    length = dp[n][m]

    index = length - 1
    ans = ''
    for k in range(1, length + 1):
        ans += '$'  # dummy string
    i = n
    j = m
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            ans = s1[i - 1] + ans[:-1]
            index -= 1
            i -= 1
            j -= 1
        elif s1[i - 1] > s2[j - 1]:
            i -= 1
        else:
            j -= 1
    return ans


s1 = "abcde"
s2 = "bdgek"
print(LCS(s1, s2))
