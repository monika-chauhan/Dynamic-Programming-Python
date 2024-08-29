# Input: expression = “T|T&F”
# Output: 1
# Explanation: The only way to get the result as true is:
# (T) | (T&F) = T|F = T
# Start with the entire block/array/expression and mark it with i, j.
# Try all partitions.
# Return the best possible answer of the two partitions (the answer that comes after dividing the problem into two
# subproblems and solving them recursively).
# left subproblem f(i, ind-1) and right sub problem f(ind+1,j) and ind
# Here f(i, ind-1) is the left sub-problem, and f(ind+1, j) is the right sub-problem. And the ind variable will start
# from i+1 and runs up to j-1 and it will move 2 steps in each iteration to select each operator at a time like the following:
# Base Case 1: We can say that when i > j this is not a valid partition and so we will return 0.
# The other base case is discussed later.
# Approach:
# The recursive algorithm steps are as follows:
# Convert the problem to a recursive function marked by the pointers i and j and the isTrue variable discussed above.
# Use a loop to check all possible partitions of the expression and calculate the total number of ways.
# Return the total number of ways calculated.
# Base case 1: If i > j, we will return 0.
# Base case 2: If i and j become equal, we will observe two different cases:
# Case 1 (If we want the number of ways of true(i.e. isTrue = 1)):
# If the single operand left is T(true), it will return 1 way and if it is F(false), it will return 0 ways.
# Case 2 (If we want the number of ways of false(i.e. isTrue = 0)):
# If the single operand left is T(true), it will return 0 ways and if it is F(false), it will return 1 way.


mod = 10 ** 9 + 7


def f(i, j, exp, isTrue):
    if i > j: return 0
    if i == j:
        if isTrue == 1:
            return exp[i] == 'T'
        else:
            return 'F'
    ways = 0
    for ind in range(i+1, j):
        leftTrue = f(i, ind-1, exp, 1)
        leftFalse = f(i,ind-1, exp, 0)
        rightTrue = f(ind+1,j,exp,1)
        rightFalse = f(ind+1,j,exp,0)

        if exp[ind] == '&':
            if isTrue == 1:
                ways = (ways + (leftTrue*rightTrue) % mod) %mod
            else:
                ways = (ways + (leftFalse*rightTrue) % mod + (leftTrue*rightFalse)%mod +(leftFalse*rightFalse)%mod)%mod
        elif exp[ind] == '|':
            if isTrue == 1:
                ways = (ways + (leftFalse * rightTrue)%mod + (leftTrue*rightFalse)%mod + (leftTrue*rightTrue)%mod)%mod
            else:
                ways = (ways + (leftFalse*rightFalse)%mod)%mod

        else:
            if isTrue == 1:
                ways = (ways + (leftTrue*rightTrue)%mod + (leftFalse * rightFalse)%mod) %mod
            else:
                ways = (ways + (leftFalse*rightTrue)%mod + (leftTrue*rightFalse)%mod) %mod
    return ways

def evaluateExp(exp):
    n = len(exp)
    return f(0,n-1,exp,1)

exp = 'F|T^F'
print(evaluateExp(exp))