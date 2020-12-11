import re


def runDayEight():
    f = open("input8.txt","r")
    txt = f.read()

    instrRgx = "([a-z]{3}) ([+-][0-9]+)"
    instrList = re.findall(instrRgx, txt)
    acc = 0
    visited = [False] * len(instrList)
    ptr = 0
    halted = False
    while not halted and not visited[ptr]:
        visited[ptr] = True
        instr = instrList[ptr][0]
        num = int(instrList[ptr][1])
        if instr == "acc":
            acc = acc + num
            ptr = ptr + 1
        elif instr == "jmp":
            ptr = ptr + num
        elif instr == "nop":
            ptr = ptr + 1
        if ptr >= len(instrList):
            halted = True
    print(acc)