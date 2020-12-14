import re

def occCount(arr, row, col):
    occNeigh = 0
    done = False
    step = 1
    while not done and row >= step and col >= step:
        if arr[row - step][col - step] == 1:
            occNeigh = occNeigh + 1
            done = True
        elif arr[row - step][col - step] == 0:
            done = True
        else:
            step = step + 1
    done = False
    step = 1
    while not done and row >= step:
        if arr[row - step][col] == 1:
            occNeigh = occNeigh + 1
            done = True
        elif arr[row - step][col] == 0:
            done = True
        else:
            step = step + 1
    done = False
    step = 1
    while not done and row >= step and col + step < len(arr[row]):
        if arr[row - step][col + step] == 1:
            occNeigh = occNeigh + 1
            done = True
        elif arr[row - step][col + step] == 0:
            done = True
        else:
            step = step + 1
    done = False
    step = 1
    while not done and col >= step:
        if arr[row][col - step] == 1:
            occNeigh = occNeigh + 1
            done = True
        elif arr[row][col - step] == 0:
            done = True
        else:
            step = step + 1
    done = False
    step = 1
    while not done and col + step < len(arr[row]):
        if arr[row][col + step] == 1:
            occNeigh = occNeigh + 1
            done = True
        elif arr[row][col + step] == 0:
            done = True
        else:
            step = step + 1
    done = False
    step = 1
    while not done and row + step < len(arr) and col >= step:
        if arr[row + step][col - step] == 1:
            occNeigh = occNeigh + 1
            done = True
        elif arr[row + step][col - step] == 0:
            done = True
        else:
            step = step + 1
    done = False
    step = 1
    while not done and row + step < len(arr):
        if arr[row + step][col] == 1:
            occNeigh = occNeigh + 1
            done = True
        elif arr[row + step][col] == 0:
            done = True
        else:
            step = step + 1
    done = False
    step = 1
    while not done and row + step < len(arr) and col + step < len(arr[row]):
        if arr[row + step][col + step] == 1:
            occNeigh = occNeigh + 1
            done = True
        elif arr[row + step][col + step] == 0:
            done = True
        else:
            step = step + 1
    return occNeigh

def runDayEleven():
    f = open("input11.txt","r")
    txt = f.read()
    rgx = "[L\.]+"
    strLayout = re.findall(rgx,txt)
    oldLayout = [[-1 for i in range(len(strLayout[0]))] for j in range(len(strLayout))]
    r = 0
    while r < len(strLayout):
        c = 0
        while c < len(strLayout[r]):
            if strLayout[r][c] == "L":
                oldLayout[r][c] = 0
            elif strLayout[r][c] == "#":
                oldLayout[r][c] = 1
            else:
                oldLayout[r][c] = -1
            c = c + 1
        r = r + 1
    done = False
    occupied = 0
    newLayout = [[-1 for i in range(len(oldLayout[0]))] for j in range(len(oldLayout))]
    while r < len(oldLayout):
        c = 0
        while c < len(oldLayout[r]):
            newLayout[r][c] = oldLayout[r][c]
            c = c + 1
        r = r + 1
    while not done:
        occupied = 0
        r = 0
        row = 0
        changed = False
        while row < len(oldLayout):
            col = 0
            while col < len(oldLayout[row]):
                if oldLayout[row][col] == 0:
                    occNeigh = occCount(oldLayout, row, col)
                    if occNeigh == 0:
                        newLayout[row][col] = 1
                        occupied = occupied + 1
                        changed = True
                    else:
                        newLayout[row][col] = 0
                elif oldLayout[row][col] == 1:
                    occNeigh = occCount(oldLayout, row, col)
                    if occNeigh >= 5:
                        newLayout[row][col] = 0
                        changed = True
                    else:
                        occupied = occupied + 1
                        newLayout[row][col] = 1
                else:
                    newLayout[row][col] = -1
                col = col + 1
            row = row + 1
        if not changed:
            done = True
        else:
            r = 0
            while r < len(newLayout):
                c = 0
                while c < len(newLayout[r]):
                    oldLayout[r][c] = newLayout[r][c]
                    c = c + 1
                r = r + 1
    print(occupied)