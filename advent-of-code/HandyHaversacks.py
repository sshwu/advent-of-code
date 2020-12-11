import re

def iterRec(idx, colorList, parList, visited):
    if parList[idx] != None:
        for color in parList[idx]:
            if color not in visited:
                visited.append(color)
                if color in colorList:
                    visited = iterRec(colorList.index(color), colorList, parList, visited)
    return visited

def childRec(idx, colorList, chiList):
    count = 1
    if chiList[idx] != None:
        for entry in chiList[idx]:
            i = colorList.index(entry[0])
            count = count + entry[1] * childRec(i, colorList, chiList)
    return count


def runDaySeven():
    f = open("input7.txt","r")
    txt = f.read()
    ruleRgx = "([a-z]+ [a-z]+) bags contain (.+)"

    ruleList = re.findall(ruleRgx, txt)
    colorList = [None] * len(ruleList)
    parList = [None] * len(ruleList)
    chiList = [None] * len(ruleList)
    count = 0

    childRgx = "([0-9]+) ([a-z]+ [a-z]+) bag"
    for rule in ruleList:
        parIdx = -1
        if rule[0] not in colorList:
            colorList[count] = rule[0]
            parIdx = count
            count = count + 1
        else:
            parIdx = colorList.index(rule[0])
        childList = re.findall(childRgx, rule[1])
        for child in childList:
            numBag = int(child[0])
            if chiList[parIdx] == None:
                chiList[parIdx] = [[child[1], numBag]]
            else:
                chiList[parIdx].append([child[1], numBag])
            if child[1] in colorList:
                idx = colorList.index(child[1])
                if parList[idx] != None:
                    parList[idx].append(rule[0])
                else:
                    parList[idx] = [rule[0]]
            else:
                colorList[count] = child[1]
                parList[count] = [rule[0]]
                count = count + 1
    sgIdx = colorList.index("shiny gold")
    visited = iterRec(sgIdx, colorList, parList, [])
    print(len(visited))
    bagCount = childRec(sgIdx, colorList, chiList) - 1
    print(bagCount)