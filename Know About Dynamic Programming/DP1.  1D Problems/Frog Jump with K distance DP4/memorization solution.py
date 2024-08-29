#  Frog Jump with K Distance/ Learn to write 1D DP
# k = 2 -> calls f(ind-1), f(ind-2)
# k  = 3 -> Calls f(ind-1), f(ind-2),f(ind-3)
# k = 4 -> calls f(ind-1),f(ind-2),f(ind-3),f(ind-4)
# every time (ind - j) if j in range(1,K):

# time = O(n*K)
# Space = O(n)

def minEnergy_frog_jump(ind, height, k, n):
    dp = [-1] * (n + 1)
    minStep = float('inf')
    if ind == 0: return ind
    if dp[ind] != -1: return dp[ind]
    for j in range(1, k + 1):
        if ind - j >= 0:
            jump = minEnergy_frog_jump(ind - j, height, k, n) + abs(height[ind] - height[ind - j])
        minStep = min(minStep, jump)
        dp[ind] = minStep
    return dp[ind]


stair = [30, 10, 60, 10, 60, 50]
n = len(stair)
k = 2
print(minEnergy_frog_jump(n - 1, stair, k, n))
