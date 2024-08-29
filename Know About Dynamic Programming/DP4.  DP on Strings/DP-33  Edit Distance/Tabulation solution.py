# We are given two strings ‘S1’ and ‘S2’. We need to convert S1 to S2. The following three operations are allowed:
# Deletion of a character.
# Replacement of a character with another one.
# Insertion of a character.
# To summarise, these are the three choices we have in case characters don’t match:
# return 1+f(i-1,j) // Insertion of character.
# return 1+f(i,j-1) // Deletion of character.
# return 1+f(i-1,j-1) // Replacement of character.
# Base Cases:
# We are reducing i and j in our recursive relation, there can be two possibilities, either i becomes -1, j becomes -1.,
# i,e we exhaust either S1 or S2 respectively.
# ex-> s1='horse' s2 = 'ros' => 3 opertaion

# time = O(n*m)
# space = O(n*m) + O(n*m)

def editDistance(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[-1] * (m+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = i
    for j in range(m+1):
        dp[0][j] = j

    for i in range(1,n+1):
        for j in range(1,m+1):

            if s1[i-1] == s2[j-1]:
                dp[i][j] = 0 + dp[i - 1][j - 1]
            else:
                replace = dp[i - 1][j - 1]  # replace of character.
                insert = dp[i - 1][j]  # Insertion of character.
                delete = dp[i][j - 1]  # Deletion of character.
                dp[i][j] = 1 + min(replace, min(insert, delete))
    return dp[n][m]


s1 = "horse"
s2 = "ros"
n = len(s1)
m = len(s2)
print(editDistance(s1, s2))
