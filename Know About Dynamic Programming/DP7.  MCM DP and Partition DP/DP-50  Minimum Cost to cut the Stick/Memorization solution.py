# Problem Description: We are given a stick of length N and a CUTS array of size C. The stick has markings as shown, and
# the CUTS array depicts the marking at which the stick needs to be cut (shown in red).
# Whenever we make a cut, we incur a cost. This cost is equal to the length of the stick on which we are making the cut.
# We need to find the minimum cost incurred to cut the stick at all the cut points.

# ex => N = 7 ,  cuts = [1,5,3,4] cust made in order = [3,5,1,4]
#                  |                                                  |
# 1 cuts = [0,1,2,3|,4,5,6,7] => cost = 7  =>  2 cuts = [0,1,2,3]  [3,4,5|,6,7] => cost = 7 + 4,
#                  |                                                  |
#              |                                                               |
# 3 cuts = [0,1|,2,3] [3,4,5] [6,7] => cost = 7 + 4 + 2 => 4 cuts [0,1] [2,3] [3, 4 |,5] [6,7] => 7 + 4 + 2 + 3 => 16
#              |                                                               |
# adding the length of stock when we cuts

def f(i, j, cuts, dp):
    if i > j: return 0
    if dp[i][j] != -1: return dp[i][j]

    mini = float('inf')
    for ind in range(i, j + 1):
        ans = cuts[j + 1] - cuts[i - 1] + f(i, ind - 1, cuts, dp) + f(ind + 1, j, cuts, dp)
        mini = min(ans, mini)
    dp[i][j] = mini
    return dp[i][j]


def minCostCuts(length, cuts):
    c = len(cuts)
    dp = [[-1] * (c + 1)] * (c + 1)
    cuts.insert(0, 0)
    cuts.append(length)
    cuts.sort()
    return f(1, c, cuts, dp)


cuts = [1, 5, 3, 4]
length = 7
print(minCostCuts(length, cuts))
