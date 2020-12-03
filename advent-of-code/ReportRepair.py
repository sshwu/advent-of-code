
# Advent of Code Puzzle 1
# Use Quicksort to sort the input array X into X_sorted.
# Make a second array Y such that Y[i] = 2020 - X_sorted[i].
# Use index trackers a and b to iterate through X_sorted and Y respectively.
# a starts at index 0 and moves forward, b starts at Y.length - 1 and moves backward.
# If X_sorted[a] = Y[b], return X_sorted[a] * X_sorted[b]
# Else if X_sorted[a] < Y[b], increment a
# Else if X_sorted[a] > Y[b], decrement b
# If a >= b, return -1
# Average runtime of nlog(n) for Quicksort, n to generate Y, n to iterate, total nlog(n) + 2n.

import re

def quicksort (arr, left, right):
    index = partition(arr, left, right)
    if left < index - 1:
        arr = quicksort(arr, left, index - 1)
    if index < right:
        arr = quicksort(arr, index, right)
    return arr

def partition (arr, left, right):
    pivot = arr[int((left+right)/2)]
    while left <= right:
        while arr[left] < pivot:
            left = left + 1
        while arr[right] > pivot:
            right = right - 1
        if left <= right:
            tmp1 = arr[left]
            tmp2 = arr[right]
            arr[left] = tmp2
            arr[right] = tmp1
            left = left + 1
            right = right - 1

    return left

def runDayOne():
    f = open("input1.txt","r")
    txt = f.read()
    inRgx = "[0-9]+"
    X_str = re.findall(inRgx, txt)
    X = []
    for s in X_str:
        X.append(int(s))
    # Use Quicksort to sort the input array X into X_sorted.
    X_sorted = quicksort(X, 0, len(X) - 1)
    # Make a second array Y such that Y[i] = 2020 - X_sorted[i].
    Y = [0] * len(X_sorted)
    count = 0
    for i in X_sorted:
        Y[count] = 2020 - i
        count = count + 1
    # Use index trackers a and b to iterate through X_sorted and Y respectively.
    a = 0
    b = len(Y) - 1
    # a starts at index 0 and moves forward, b starts at Y.length - 1 and moves backward.
    while a < b:
    # If X_sorted[a] = Y[b], return X_sorted[a] * X_sorted[b]
        if X_sorted[a] == Y[b]:
            print(X_sorted[a] * X_sorted[b])
            a = len(Y)
    # Else if X_sorted[a] < Y[b], increment a
        elif X_sorted[a] < Y[b]:
            a = a + 1
    # Else if X_sorted[a] > Y[b], decrement b
        else:
            b = b - 1
    # If a >= b, return -1
    if a == b:
        print("-1")

    index = 0
    done = False
    for j in X_sorted:
        if not done:
            diff = 2020 - j
            a = index + 1
            b = len(X_sorted) - 1
            while a < b:
                if X_sorted[a] == diff - X_sorted[b]:
                    print(j * X_sorted[a] * X_sorted[b])
                    a = len(X_sorted)
                    done = True
                elif X_sorted[a] < diff - X_sorted[b]:
                    a = a + 1
                else:
                    b = b - 1