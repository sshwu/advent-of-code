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

def travRec(arr, mem, idx):
    if mem[idx] != None:
        return mem[idx]
    count = 0
    if idx == len(arr) - 1:
        return 1
    if arr[idx+1] > arr[idx] + 3:
        mem[idx] = 0
        return count
    else:
        count = count + travRec(arr, mem, idx + 1)
        if idx < len(arr) - 3 and arr[idx+2] <= arr[idx] + 3:
            count = count + travRec(arr, mem, idx + 2)
            if idx < len(arr) - 4 and arr[idx+3] == arr[idx] + 3:
                count = count + travRec(arr, mem, idx + 3)
        mem[idx] = count
        return count


def runDayTen():
    f = open("input10.txt","r")
    txt = f.read()
    numRgx = "[0-9]+"
    numStrList = re.findall(numRgx, txt)
    numList = [0] * (len(numStrList) + 2)
    i = 1
    maxVal = 0
    for numStr in numStrList:
        numList[i] = int(numStr)
        if numList[i] > maxVal:
            maxVal = numList[i]
        i = i + 1
    numList[len(numList) - 1] = maxVal + 3
    numList = quicksort(numList, 0, len(numList) - 1)
    prev = 0
    ptr = 0
    jolt1 = 0
    jolt3 = 0
    for a in numList:
        diff = a - prev
        if diff == 1:
            jolt1 = jolt1 + 1
        elif diff == 3:
            jolt3 = jolt3 + 1
        prev = a
    print(jolt1 * jolt3)

    mem = [None] * len(numList)
    ans = travRec(numList, mem, 0)
    print(ans)