# We are given two strings ‘S1’ and ‘S2’. We need to return their shortest common supersequence. A supersequence is
# defined as the string which contains both the strings S1 and S2 as subsequences.
# ex-> s1 = 'brute' s2 = 'groot' => common take one time and combine both string => 'bgruoote'
# To frame the string, we need to understand how the dp table was formed and work in the reverse process.
# Now, let us see what were the conditions that we used while forming the dp array:
# if(S1[i-1] == S2[j-1]), then return 1 + dp[i-1][j-1]
# if(S1[i-1] != S2[j-1]) , then return 0 + max(dp[i-1][j],dp[i][j-1])

# To form the string, we will work in a reverse manner.
# if(S1[i-1] == S2[j-1]), this means the character is an lcs character and needs to be included only once from both
# the strings, so we add it to the ans string and reduce both i and j by 1. We reduce them simultaneously to make sure
# the character is counted only once.
# if(S1[i-1] != S2[j-1]), this means that the character is a non-lcs character and then we move the pointer to the top
# cell or left cell depending on which is greater. This way non-lcs characters will be included separately in the right
# order.

# Time Complexity: O(N*M)
# Reason: There are two nested loops
# Space Complexity: O(N*M)

def shortestSupersequence(s1, s2):
    n = len(s1)
    m = len(s2)

    dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 0
    for i in range(m + 1):
        dp[0][i] = 0

    for ind1 in range(1, n + 1):
        for ind2 in range(1, m + 1):
            if s1[ind1 - 1] == s2[ind2 - 1]:
                dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
            else:
                dp[ind1][ind2] = 0+ max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])

    # printing the super-sequence
    len_ = dp[n][m]
    i = n
    j = m

    index = len_ - 1
    ans = ""

    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            ans += s1[i - 1]
            index -= 1
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            ans += s1[i - 1]
            i -= 1
        else:
            ans += s2[j - 1]
            j -= 1
    #Adding Remaing Characters - Only one of the below two while loops will run
    while i > 0:
        ans += s1[i - 1]
        i -= 1
    while j > 0:
        ans += s2[j - 1]
        j -= 1

    ans=ans[::-1]
    return ans


s1 = "brute"
s2 = "groot"
print("The Longest Common Supersequence is " + shortestSupersequence(s1, s2))
