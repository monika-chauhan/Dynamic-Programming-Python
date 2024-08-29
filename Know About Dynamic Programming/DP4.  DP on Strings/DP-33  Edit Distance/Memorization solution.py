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
def editDistance(i, j, s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[-1] * (m+1) for _ in range(n+1)]
    if i < 0:
        return j + 1;
    if j < 0:
        return i + 1;
    if dp[i][j] != -1: return dp[i][j]

    if s1[i] == s2[j]:
        dp[i][j] = 0 + editDistance(i - 1, j - 1, s1, s2)
    else:
        replace = editDistance(i - 1, j - 1, s1, s2)  # replace of character.
        insert = editDistance(i - 1, j, s1, s2)  # Insertion of character.
        delete = editDistance(i, j - 1, s1, s2)  # Deletion of character.
        dp[i][j] = 1 + min(replace, min(insert, delete))
    return dp[i][j]


s1 = "horse"
s2 = "ros"
n = len(s1)
m = len(s2)
print(editDistance(n - 1, m - 1, s1, s2))
