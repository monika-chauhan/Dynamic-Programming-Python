# We are given two strings ‘S1’ and ‘S2’. String S1 can have the following two special characters:
# ‘?’ can be matched to a single character of S2.
# ‘*’ can be matched to any sequence of characters of S2. (sequence can be of length zero or more).
# We need to check whether strings S1 and S2 match or not.
# ex-> s1 = '?ay' , s2 = 'ray' => True => ? = r so true
# s1 = '**abcd' s2 = 'abcd' => True => ** = '' (empty string) True
# s1 = 'ab*cd' s2 = 'abdefed' => True  => * => def ( True)
# s1 = 'ab?d' s2 = 'abcc' => False => ? = c but d != c (False)

# Either the characters match already.
# Or, if there is a ‘?’, we can explicitly match a single character.
# For a ‘*’, the following figure explains the scenario.

# (i).When the characters match
# if(S1[i]==S2[j]),  => f(i-1,j-1)
# (ii) When the characters don’t match
# If the characters don’t match, there are three possible scenarios:
# S1[i] == ‘?’
# S1[i] == ‘*’
# S1[i] is some other character
# Call f(i-1,j). i.e replace ‘*’ with nothing and act as if it was not present.
# Call f(i,j-1). i.e replace ‘*’ with a single character at index j and make the i pointer to still point at index i.
# In this, we matched it with a single character (one of the many options that need to be tried) and in the next
# recursive call, as i still point to ‘*’, we get the exact two recursive calls again.
# (iii) If S1[i] is neither ‘?’ nor ‘*’
# To summarise:
#
# If S1[i] == ‘?’, return f(i-1,j)
# Else if S1[i] == ‘*’, return f(i-1,j) || f(i,j-1)
# Else return false
# Base Cases:
# We are reducing i and j in our recursive relation, there can be two possibilities,either i becomes -1 or j becomes -1.
# , i,e we exhaust either S1 or S2 respectively.
# (i) When S1 is exhausted:
# if(i<0 && j<0), return true.
# if(i<0 && j>=0), return false.

# (ii) When S2 is exhausted:
# When S2 is exhausted(j<0) and S1 has not, there is only one pattern that can account for true(matching of strings).
# It is if S1 is like this “*”,”****”,”***”, i.e: S1 contains only stars. Then we can replace every star with a sequence
# of length 0 and say that the string match.
# If S1 is all-stars, we return true, else return false.
# time = O(n*m)
# Space = O(n*m) +O(n+m)

def isAllStars(s1, i):
    for j in range(i+1):
        if s1[j] != '*':
            return False
    return True


def wildCardMatching(i, j, S1, S2):
    n = len(S1)
    m = len(S2)
    dp = [[-1]*(m+1) for _ in range(n+1)]
    # Base Conditions
    if i < 0 and j < 0:
        return True
    if i < 0 and j >= 0:
        return False
    if j < 0 and i >= 0:
        return isAllStars(S1, i);

    if dp[i][j] != -1: return dp[i][j]

    if S1[i] == S2[j] or  S1[i] == '?':
        dp[i][j] = wildCardMatching(i - 1, j - 1, S1, S2);
    else:
        if S1[i] == '*':
            return wildCardMatching( i - 1, j, S1, S2) or wildCardMatching(i, j - 1, S1, S2)
        else:
            return False
    return dp[i][j]

s1 = 'ab?d'
s2 = 'abcc'
s11 = "ab*cd"
s22 = "abdefcd"
n = len(s11)
m = len(s22)
print(wildCardMatching(n - 1, m - 1, s11, s22))
