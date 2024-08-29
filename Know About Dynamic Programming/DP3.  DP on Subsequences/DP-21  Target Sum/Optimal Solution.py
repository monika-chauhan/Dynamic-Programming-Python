# We are given an array ‘ARR’ of size ‘N’ and a number ‘Target’. Our task is to build an expression from the given array
# where we can place a ‘+’ or ‘-’ sign in front of an integer. We want to place a sign in front of every integer of the
# array and get our required target. We need to count the number of ways in which we can achieve our required target.


# ex = [1,2,3,1] target = 3
# assign sign(-,+)  1 ways => -1,+2,+3,-1 => 5 , Second ways=> +1, -2, +3, +1 => 5 Total Ways = 2
# we are breaking array into two subset and make target of adding both s1 - s2 = target
# Same problem as Count Partition With given Difference s1-s2 = D
# s2 = (totalSum - D)//2 => target

# Base Cases:
# If target == 0, it means that we have already found the subsequence from the previous steps, so we can return 1.
# If ind==0, it means we are at the first element, so we need to return arr[ind]==target. If the element is equal to the
# target we return 1 else we return 0.

# Time Complexity: O(N*K)
# Space Complexity: O(K)

def countPartitionsUtil(target, arr, n):
    prev = [0] * (target + 1)
    curr = [0] * (target + 1)

    if arr[0] == 0:
        prev[0] = 2  # 2 cases - pick and not pick
    else:
        prev[0] = 1

    if arr[0] != 0 or arr[0] <= target:
        prev[arr[0]] = 1  # 1 case - pick

    for ind in range(1, n):
        for tar in range(target + 1):
            notTaken = prev[tar]

            taken = 0
            if arr[ind] <= tar:
                taken = prev[tar - arr[ind]]

            curr[tar] = (notTaken + taken)
        prev = curr[:]
    return prev[target]


def countPartitions(d, arr):
    n = len(arr)
    totSum = sum(arr)

    # Checking for edge cases
    if totSum - d < 0 or (totSum - d) % 2 == 1:
        return 0
    s2 = (totSum - d) // 2

    return countPartitionsUtil(s2, arr, n)


def TargetSum(array, target):
    return countPartitions(target, array)


arr = [1, 2, 3, 1]
target = 3

print("The number of ways found is", TargetSum(arr, target))
