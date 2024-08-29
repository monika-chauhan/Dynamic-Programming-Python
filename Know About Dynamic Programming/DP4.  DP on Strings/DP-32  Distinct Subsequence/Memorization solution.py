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
# SPace = O(n*m) + O(n+m)
def DistinctsubsequenceCounting(i, j, s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[-1]*(m+1) for _ in range(n+1)]
    if j < 0: return 1
    if i < 0: return 0
    if dp[i][j] != -1: return dp[i][j]
    if s1[i - 1] == s2[j - 1]:
       dp[i][j] = DistinctsubsequenceCounting(i - 1, j - 1, s1, s2) + DistinctsubsequenceCounting(i - 1, j, s1, s2)
    else:
        dp[i][j] = DistinctsubsequenceCounting(i-1, j, s1, s2)
    return dp[i][j]

s1 = 'babgbag'
s2 = 'bag'
n = len(s1)
m = len(s2)
print(DistinctsubsequenceCounting(n - 1, m - 1, s1, s2))
