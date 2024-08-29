# find length of  Longest common substring

def LCS(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    max_len = 0
    end_index = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                if dp[i][j] > max_len and (n - j + dp[i][j] - 1) == (i - 1):
                    max_len = dp[i][j]
                    end_index = i - 1
            else:
                dp[i][j] = 0
    return max_len, end_index


def printLongestPalindromeSubString(s):
    t = s[::-1]
    max_len, end_index = LCS(s, t)
    return s[end_index - max_len + 1: end_index + 1]


print(printLongestPalindromeSubString('"aacabdkacaa"'))
