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

def findSum(arr, target):
    found = False
    lo = 0
    hi = len(arr) - 1
    while not found and lo < hi:
        if arr[lo] == target - arr[hi]:
            found = True
        elif arr[lo] < target - arr[hi]:
            lo = lo + 1
        else:
            hi = hi - 1
    return found

def runDayNine():
    f = open("input9.txt","r")
    txt = f.read()
    numRgx = "[0-9]+"
    numStrList = re.findall(numRgx, txt)
    numList = [0] * len(numStrList)
    i = 0
    for numStr in numStrList:
        numList[i] = int(numStr)
        i = i + 1
    tailIdx = 0
    headIdx = 24
    subArr = numList[tailIdx:headIdx+1]
    subArr = quicksort(subArr, tailIdx, headIdx)
    done = False
    idx = headIdx + 1
    ans = -1
    while not done and idx < len(numList):
        ans = numList[idx]
        found = findSum(subArr, numList[idx])
        if found:
            idx = idx + 1
            headIdx = headIdx + 1
            tailIdx = tailIdx + 1
            subArr = numList[tailIdx:headIdx+1]
            subArr = quicksort(subArr, 0, 24)
        else:
            done = True
    print(ans)
    found = False
    sumList = [0] * (len(numList) + 1)
    i = 1
    while i <= len(numList):
        sumList[i] = numList[i-1] + sumList[i-1]
        i = i + 1
    startPtr = 0
    endPtr = 1
    while not found:
        done = False
        while not done:
            sum = sumList[endPtr + 1] - sumList[startPtr]
            if sum == ans:
                done = True
                found = True
            elif sum < ans:
                if endPtr == len(numList) - 1:
                    done = True
                else:
                    endPtr = endPtr + 1
            else:
                done = True
        if not found:
            startPtr = startPtr + 1
            endPtr = startPtr + 1
    subArr = numList[startPtr:endPtr+1]
    subArr = quicksort(subArr, 0, len(subArr) - 1)
    print(subArr[0] + subArr[len(subArr)-1])