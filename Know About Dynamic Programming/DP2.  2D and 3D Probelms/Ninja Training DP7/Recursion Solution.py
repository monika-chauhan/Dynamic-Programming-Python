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


def NinjaTraining(day, last, point):
    # base case
    if day == 0:  # if we have only day= 0 then we can perform the maximum value activity
        maxi = 0
        for i in range(3):  # we have 3 activity to perform 0,1,2
            if last != i:  # if the last activity not equal to current activity
                maxi = max(maxi, point[0][i])
        return maxi
    maxi = 0
    activity = 0
    for i in range(3):
        if last != i:
            activity = point[day][i] + NinjaTraining(day - 1, i, point)
        maxi = max(maxi, activity)
    return maxi


points = [[10, 40, 70], [20, 50, 80], [30, 60, 90]]
day = len(points)
print(NinjaTraining(day-1, 3, points))
