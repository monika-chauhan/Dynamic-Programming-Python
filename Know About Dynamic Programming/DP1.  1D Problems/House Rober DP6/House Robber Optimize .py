# A thief needs to rob money in a street. The houses in the street are arranged in a circular manner. Therefore the
# first and the last house are adjacent to each other. The security system in the street is such that if adjacent
# houses are robbed, the police will get notified.

# Given an array of integers “Arr” which represents money at each house, we need to return the maximum amount of money
# that the thief can rob without alerting the police.

# N = 4 , a = [2,1,4,9] => pick a[1] + pick a[3] =max(1+9,0)= 10
# N = 5, a = [1,5,2,1,6] => pick a[1] + pick a[4] => max(5+6,0) = 11

# Algo
# 1.Make two reduced arrays – arr1(arr-last element) and arr2(arr-first element).
# 2.Find the maximum of non-adjacent elements as mentioned in article DP5 on arr1 and arr2 separately. Let’s call the
# answers we got ans1 and ans2 respectively.
# 3.Return max(ans1, ans2) as our final answer.
# house Robber we can say => max Sum Non-Adjacent problem but in circular manner so make two array 1. arr[0:len(a)-1]
# and 2.arr[1:]


# Time = O(n)
# space = O(1)

def maxSumNonAdj(a, n):
    prev0 = 0
    prev1 = a[0]
    for ind in range(1, n):
        pick = a[ind]
        if ind > 1:
            pick = a[ind] + prev0
        notPick = 0 + prev1
        curr = max(pick, notPick)
        prev0 = prev1
        prev1 = curr
    return prev1


def HouseRobber(a, n):
    a1 = a[0:n - 1]
    a2 = a[1:n]
    ans1 = maxSumNonAdj(a1, len(a1))
    ans2 = maxSumNonAdj(a2, len(a2))
    return max(ans1, ans2)


a = [2, 3, 2]
b = [1, 5, 2, 1, 6]
print(HouseRobber(a, len(a)))
print(HouseRobber(b, len(b)))
