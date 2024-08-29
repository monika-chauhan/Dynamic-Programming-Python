# Given a number of stairs and a frog, the frog wants to climb from the 0th stair to the (N-1)th stair. At a time the
# frog can climb either one or two steps. A height[N] array is also given. Whenever the frog jumps from a stair i to
# stair j, the energy consumed in the jump is abs(height[i]- height[j]), where abs() means the absolute difference.
# We need to return the minimum energy that can be used by the frog to jump from stair 0 to stair N-1.

# time = O(n)
# space = O(1)

def minEnergy_frogJump(height, n):
    prev0 = 0
    prev1 = 0
    for ind in range(1, n):
        oneJump = prev1 + abs(height[ind] - height[ind - 1])
        twoJump = float('inf')
        if ind > 1:
            twoJump = prev0 + abs(height[ind] - height[ind - 2])
        curr = min(oneJump, twoJump)

        prev0 = prev1
        prev1 = curr

    return prev1


stair = [30, 10, 60, 10, 50]
n = len(stair)
print(minEnergy_frogJump(stair, n))
