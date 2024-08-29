#  Frog Jump with K Distance/ Learn to write 1D DP
# k = 2 -> calls f(ind-1), f(ind-2)
# k  = 3 -> Calls f(ind-1), f(ind-2),f(ind-3)
# k = 4 -> calls f(ind-1),f(ind-2),f(ind-3),f(ind-4)
# every time (ind - j) if j in range(1,K):
def minStep_frog_jump(ind, height, k):
    if ind == 0: return 0
    minStep = float('inf')
    for j in range(1, k + 1):
        if ind - j >= 0:
            jump = minStep_frog_jump(ind - j, height, k) + abs(height[ind] - height[ind - j])
        minStep = min(minStep, jump)
    return minStep


stair = [30, 10, 60, 10, 60, 50]
k = 2
n = len(stair)
print(minStep_frog_jump(n - 1, stair, k))
