import re

def runDayTwelve():
    f = open("input12.txt","r")
    txt = f.read()
    rgx = "([A-Z])([0-9]+)"
    instrList = re.findall(rgx, txt)
    shipX = 0
    shipY = 0
    wpX = 10
    wpY = 1
    for instr in instrList:
        if instr[0] == "N":
            wpY = wpY + int(instr[1])
        elif instr[0] == "S":
            wpY = wpY - int(instr[1])
        elif instr[0] == "E":
            wpX = wpX + int(instr[1])
        elif instr[0] == "W":
            wpX = wpX - int(instr[1])
        elif instr[0] == "L":
            if int(instr[1]) == 90:
                oldY = wpY
                oldX = wpX
                wpY = oldX
                wpX = -1 * oldY
            elif int(instr[1]) == 180:
                oldY = wpY
                oldX = wpX
                wpY = -1 * oldY
                wpX = -1 * oldX
            elif int(instr[1]) == 270:
                oldY = wpY
                oldX = wpX
                wpY = -1 * oldX
                wpX = oldY
        elif instr[0] == "R":
            if int(instr[1]) == 90:
                oldY = wpY
                oldX = wpX
                wpY = -1 * oldX
                wpX = oldY
            elif int(instr[1]) == 180:
                oldY = wpY
                oldX = wpX
                wpY = -1 * oldY
                wpX = -1 * oldX
            elif int(instr[1]) == 270:
                oldY = wpY
                oldX = wpX
                wpY = oldX
                wpX = -1 * oldY
        elif instr[0] == "F":
            for i in range(int(instr[1])):
                shipX = shipX + wpX
                shipY = shipY + wpY
    print(abs(shipX) + abs(shipY))