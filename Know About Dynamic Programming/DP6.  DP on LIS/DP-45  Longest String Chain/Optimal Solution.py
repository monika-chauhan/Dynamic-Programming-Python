# Problem Statement: We are given an array of strings (sat words[ ]), and we need to return the longest string
# chain. This longest string chain is defined as:
# A subsequence of words[ ] of the string.
# Every element of this subsequence ( a string) except the first one can be formed by inserting a single character into
# the previous element.
# The first element of this subsequence can be any string from the words[ ] array.
# Two consecutive strings in this string chain need to have an insertion of a single character. The character can be
# added to any place on the string.
# There we used to compare two elements of the array and consider the previous element of the array if it was smaller
# than the current element.
# In this problem, we will use the same technique and compare two values of the array and consider the previous element
# of the array, if it is just one character deletion from the current element.

# Solution :
# There we used to compare two elements of the array and consider the previous element of the array if it was smaller
# than the current element.
# In this problem, we will use the same technique and compare two values of the array and consider the previous element
# of the array, if it is just one character deletion from the current element.

# compare( S1, S2)
# It returns true if the first string S1 is just a single character addition with S2 else it returns false. The way
# we have called the code, we expect S1 to be the larger string of the two. Therefore the length of S1 should be
# greater than the length of S2 by 1. After checking for the length we can do a character matching using a
# two-pointer approach. We will declare two pointers first and second, initially set to the first index of S1 and S2
# respectively. Then we set a while loop which will run till the first is less than the length of S1. In every
# iteration, if both the characters match, i.e S1[first] == S2[second], we increment both first and second by1. Else,
# we will increment only first by 1. As S1’s length(say m) is just greater than S2’s length(say n) by 1 using the
# above pointer approach both the pointers should point to m and n simultaneously. If it happens we return true,
# else we return fals
# array = ["a", "b", "ba", "bca", "bda", "bdca"] s1 = a , s2 = 'ba' => compare => a != b: then s2 += 1 => 1 , a == b:
# s2 += 1 => 2 ,s1 += 1 => 1 => s1 + 1 == s2 => true
# s1 = ba , s2 = 'bca' => compare => b == b: s1 += 1 => 1, s2 += 1 => 1,
# a != c: s2 += 1 => 2, a == a: s2 += 1 => 3, s1 += 1 => 2 , s1 + 1(2) == s2(3) : return True
# s1 = 'bca' , s2 = 'bcda' => b == b s1 += 1 => 1, s2 += 1=1 => c == c: s1 += 1 => 2, s2 += 1 => 2,
# a == d: s2 += 1 => 3, a == a: => s1 += 1 => 3, s2 += 1 => 4
# if s1 + 1 == s2: return True, return False

# time = O(n*n)
# Space = O(n)

def compare(s1, s2):
    if len(s1) != len(s2) + 1: return False
    first = second = 0
    while first < len(s1):
        if second < len(s2) and s1[first] == s2[second]:
            first += 1
            second += 1
        else:
            first += 1
    if first == len(s1) and second == len(s2):
        return True
    return False


def LongestStringChain(array):
    n = len(array)
    dp = [1] * (n)
    array.sort()
    maxi = 1
    for ind in range(n):
        for prev_ind in range(ind):
            if compare(array[ind], array[prev_ind]) and 1 + dp[prev_ind] > dp[ind]:
                dp[ind] = 1 + dp[prev_ind]

        if dp[ind] > maxi:
            maxi = dp[ind]
    return maxi


array = ["a", "b", "ba", "bca", "bda", "bdca"]
print(LongestStringChain(array))
