# We are given two strings S1 and S2, we want to know how many distinct subsequences of S2 are present in S1.
# ex => s1 = 'babgbag' s2 = 'bag' How can time s2 occurs ans = 5 times
# We have to find distinct subsequences of S2 in S1. As there is no uniformity in data, there is no other way to find
# out than to try out all possible ways. To do so we will need to use recursion.
# This can be summarized as :
# if(S1[i]==S2[j]), call f(i-1,j-1) and f(i-1,j).
# if(S1[i]!=S2[j]), call f(i-1,j).
# As we have to return the total count, we will return the sum of f(i-1,j-1) and f(i-1,j) in case 1 and simply
# return f(i-1,j) in case 2.
# Base Cases:
# We are reducing i and j in our recursive relation, there can be two possibilities, either i becomes -1,j becomes -1.
# if j<0, it means we have matched all characters of S2 with characters of S1, so we return 1.
# if i<0, it means we have checked all characters of S1 but we are not able to match all characters of S2,
# therefore we return 0.
# time = O(n*m)
# space = O(m*n)

def DistinctsubsequenceCounting( s1, s2):
    n = len(s1)
    m = len(s2)
    dp =[[0]*(m+1) for _ in range(n+1)]
    for i in range(n + 1):
        dp[i][0] = 1
    for i in range(1, m + 1):
        dp[0][i] = 0

    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][m]


s1 = 'babgbag'
s2 = 'bag'
n = len(s1)
m = len(s2)
print(DistinctsubsequenceCounting(s1, s2))
