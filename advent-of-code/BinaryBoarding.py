import re

def runDayFive():
    f = open("input5.txt","r")
    txt = f.read()
    rgx = "[BF]{7}[LR]{3}"
    bpList = re.findall(rgx, txt)
    idMax = 0
    present = [False] * (128 * 8)
    for bp in bpList:
        rowMin = 0
        rowMax = 127
        colMin = 0
        colMax = 7
        for i in range(len(bp)):
            if bp[i] == "F":
                rowMax = int((rowMax + rowMin - 1) / 2)
            elif bp[i] == "B":
                rowMin = int((rowMax + rowMin + 1) / 2)
            elif bp[i] == "L":
                colMax = int((colMax + colMin - 1) / 2)
            else:
                colMin = int((colMax + colMin + 1) / 2)

        id = rowMin * 8 + colMin
        present[id] = True
        if id > idMax:
            idMax = id
    print(idMax)
    found = False
    idx = 8
    while not found and idx < len(present) - 1:
        if not present[idx] and present[idx - 1] and present[idx + 1]:
            found = True
        else:
            idx = idx + 1
    print(idx)