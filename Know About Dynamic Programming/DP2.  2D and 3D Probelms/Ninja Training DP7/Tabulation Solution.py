# A Ninja has an ‘N’ Day training schedule. He has to perform one of these three activities (Running, Fighting Practice,
# or Learning New Moves) each day. There are merit points associated with performing an activity each day. The same
# activity can’t be performed on two consecutive days. We need to find the maximum merit points the ninja can attain in
# N Days.
#
# We're given a 2D Array POINTS of size ‘N*3’ which tells us the merit point of specific activity on that particular
# day. Our task is to calculate the maximum number of merit points that the ninja can earn.

# day    d0  d1  d2
# 0          1    2
# 1      0        2
# 2      0    1        => We have 2 choice
# 3      0    1    2  => Last day we have all choice
# day = 3 (work as index)
# points = [d0,d1,d2] # if we perform day1 => d0 then we can't perform d0 on next day
# points = [10,40,70],[20,50,80],[30,60,90]
# we need to f(day, last) => last = perform last day activity either 0,1 or 2

# time = O(n * 4 * 3)
# Space = O(n)  + O(n*4)

def NinjaTraining(n, points):
    dp = [[0 for j in range(4)] for i in range(n)]

    dp[0][0] = max(points[0][1], points[0][2])
    dp[0][1] = max(points[0][0], points[0][2])
    dp[0][2] = max(points[0][0], points[0][1])
    dp[0][3] = max(points[0][0], max(points[0][1], points[0][2]))

    for day in range(1, n):
        for last in range(4):
            dp[day][last] = 0
            for task in range(3):
                if task != last:
                    activity = points[day][task] + dp[day - 1][task]
                    dp[day][last] = max(dp[day][last], activity)

    return dp[n - 1][3]


points = [[10, 40, 70], [20, 50, 80], [30, 60, 90]]
day = len(points)
print(NinjaTraining(day, points))
