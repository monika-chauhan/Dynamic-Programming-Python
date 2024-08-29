# Approach:
#
# Now, as we have understood the entire intuition of the algorithm we will summarize the approach:
#
# Initialize a temp array.
# Push the first element of the array to temp.
# Iterate over the next elements.
# In every iteration, if arr[i] is greater than the last element of the temp array simply push it to the temp array.
# Else, just find the lower_bound index (where we can insert that element) of that element in the temp array (say ind).
# THen simply initialize temp[ind] = arr[i] (// replacement step).
# Maintain a len variable to calculate the length of the temp array in the iteration itself.
# Time = O(n*logn)
# Space = O(n)

from bisect import bisect_left


def LIS_binarySearch(array):
    n = len(array)
    temp = [array[0]]
    length = 1
    for i in range(1, n):
        if array[i] > temp[-1]:
            temp.append(array[i])
            length += 1
        else:
            insert_ind = bisect_left(temp, array[i], lo=0, hi=len(temp))
            temp[insert_ind] = array[i]
    return length


array = [10, 9, 2, 5, 3, 7, 101, 18]
print(LIS_binarySearch(array))


def LIS_bin(array):
    n = len(array)
    res = []
    for i, val in enumerate(array):
        idx = bisect_left(res, val)
        if idx == len(res):
            res.append(val)
        else:
            res[idx] = val
    return len(res)


array = [10, 9, 2, 5, 3, 7, 101, 18]
print(LIS_bin(array))
