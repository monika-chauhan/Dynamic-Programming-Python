# Algo
# So rather than storing the entire 2D Array of size N*4, we can just store values of size 4(say prev).
# We can then take a dummy array, again of size 4 (say temp) and calculate the next row’s value using the array we
# stored in step 1.
# After that whenever we move to the next day, the temp array becomes our prev for the next step.
# At last prev[3] will give us the answer.

# time = O(n*4*3)
# space = O(3)
def NinjaTraining(Noday, points):
    prev = [0] * 4
    prev[0] = max(points[0][1], points[0][2])
    prev[1] = max(points[0][0], points[0][2])
    prev[2] = max(points[0][0], points[0][1])
    prev[3] = max(points[0][0], max(points[0][1], points[0][2]))

    for day in range(1, Noday):
        temp = [0] * 4
        for last in range(4):
            temp[last] = 0
            for cur_act in range(3):
                if cur_act != last:
                    temp[last] = max(temp[last], points[day][cur_act] + prev[cur_act])

        prev = temp
    return prev[3]


points = [[10, 40, 70], [20, 50, 80], [30, 60, 90]]
day = len(points)
print(NinjaTraining(day, points))
