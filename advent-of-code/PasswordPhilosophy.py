import re


def runDayTwo():
    f = open("input2.txt","r")
    txt = f.read()
    regex = "([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)"
    pwList = re.findall(regex, txt)
    validCount = 0
    for entry in pwList:
        min = int(entry[0])
        max = int(entry[1])
        letter = entry[2]
        pw = entry[3]
        letterCount = 0
        for i in range(len(pw)):
            if letter == pw[i]:
                letterCount = letterCount + 1
        if letterCount >= min and letterCount <= max:
            validCount = validCount + 1
    print(validCount)

    validCount = 0
    for entry in pwList:
        idx1 = int(entry[0])
        idx2 = int(entry[1])
        letter = entry[2]
        pw = entry[3]
        if pw[idx1 - 1] == letter and pw[idx2 - 1] != letter:
            validCount = validCount + 1
        elif pw[idx1 - 1] != letter and pw[idx2 - 1] == letter:
            validCount = validCount + 1
    print(validCount)