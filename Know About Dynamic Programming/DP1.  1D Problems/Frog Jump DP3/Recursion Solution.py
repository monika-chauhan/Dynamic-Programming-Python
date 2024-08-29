# Given a number of stairs and a frog, the frog wants to climb from the 0th stair to the (N-1)th stair. At a time the
# frog can climb either one or two steps. A height[N] array is also given. Whenever the frog jumps from a stair i to
# stair j, the energy consumed in the jump is abs(height[i]- height[j]), where abs() means the absolute difference.
# We need to return the minimum energy that can be used by the frog to jump from stair 0 to stair N-1.

def min_energy_by_frog_jump(ind, height):
    if ind == 0:
        return 0
    oneJump = min_energy_by_frog_jump(ind - 1, height) + abs(height[ind] - height[ind - 1])
    twoJump = float('inf')
    if ind > 1:
        twoJump = min_energy_by_frog_jump(ind - 2, height) + abs(height[ind] - height[ind - 2])
    return min(oneJump ,twoJump)


stair = [30, 10, 60, 10, 60, 50]
n = len(stair)
print(min_energy_by_frog_jump(n-1, stair))
