# Given a number of stairs. Starting from the 0th stair we need to climb to the “Nth” stair. At a time we can climb
# either one or two steps. We need to return the total number of distinct ways to reach from 0th to Nth stair.

def climb_stair(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climb_stair(n - 1) + climb_stair(n - 2)


print(climb_stair(3))
