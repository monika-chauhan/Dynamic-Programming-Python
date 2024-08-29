# Minimum Insertions/Deletions to Convert String A to String B
# We are given two strings, str1 and str2. We are allowed the following operations:
# Delete any number of characters from string str1.
# Insert any number of characters in string str1.
# We need to tell the minimum operations required to convert str1 to str2.
# ex-> s1 = 'abcd' s2= 'anc' -> LCS(s1,s2) => ac , removeOp => len(s1) - LCS(s1,s2) and insertOP = len(s2)- lCS(s1,s2)
# add removeOp + insertOp

# The algorithm is stated as follows:
# Let n and m be the length of str1 and str2 respectively.
# Find the length of the longest common subsequence ( say k) of str1 and str2 as discussed in  Longest Common Subsequence.
# Return (n-k) + (m-k) as answer.

# Time Complexity: O(N*M)
# Reason: There are two nested loops
# Space Complexity: O(M)
def LCS(s1,s2):
    n = len(s1)
    m = len(s2)
    prev = [0 for _ in range(m+1)]
    curr = [0 for _ in range(m+1)]  # Base case covered as assign 0

    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[i-1] == s2[j-1]:
                curr[j] = 1 + prev[j-1]
            else:
                curr[j] = max(prev[j],curr[j-1])
        prev = curr[:]
    return prev[m]

def minInsertDeleteOpertionToMakeString(s1, s2):
    deleteOP = len(s1) - LCS(s1,s2)
    insertOP = len(s2) - LCS(s1,s2)
    return insertOP + deleteOP

s1 = 'abcd'
s2 = 'anc'
print(minInsertDeleteOpertionToMakeString(s1,s2))
