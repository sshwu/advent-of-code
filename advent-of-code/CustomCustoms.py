import re

def runDaySix():
    f = open("input6.txt","r")
    txt = f.read()
    ansRgx = "(?:[a-z]+\n)+(?:[a-z]+)*"

    ansList = re.findall(ansRgx, txt)
    sumCount = 0
    for ans in ansList:
        subRgx = "[a-z]+"
        subList = re.findall(subRgx, ans)
        answered = subList[0]
        removeList = []
        for sub in subList:
            for i in range(len(answered)):
                if answered[i] not in sub and answered[i] not in removeList:
                    removeList.append(answered[i])
        sumCount = sumCount + len(answered) - len(removeList)
    print(sumCount)