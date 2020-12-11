import re

def execute(instrList, flipIdx):
    acc = 0
    visited = [False] * len(instrList)
    ptr = 0
    valid = False
    while not valid and not visited[ptr]:
        visited[ptr] = True
        instr = instrList[ptr][0]
        num = int(instrList[ptr][1])
        if instr == "acc":
            acc = acc + num
            ptr = ptr + 1
        elif instr == "jmp":
            if ptr != flipIdx:
                ptr = ptr + num
            else:
                ptr = ptr + 1
        elif instr == "nop":
            if ptr != flipIdx:
                ptr = ptr + 1
            else:
                ptr = ptr + num
        if ptr == len(instrList):
            valid = True
    return [valid, acc]

def runDayEight():
    f = open("input8.txt","r")
    txt = f.read()

    instrRgx = "([a-z]{3}) ([+-][0-9]+)"
    instrList = re.findall(instrRgx, txt)
    idx = 0
    done = False
    acc = -1
    while not done and idx < len(instrList):
        if instrList[idx][0] == "jmp" or instrList[idx][0] == "nop":
            done, acc = execute(instrList, idx)
            if not done:
                idx = idx + 1
        else:
            idx = idx + 1
    print(acc)