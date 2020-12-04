import re

def runDayFour():
    f = open("input4.txt","r")
    txt = f.read()
    ppRgx = "(?:.+\n)+(?:.+)*"
    ppList = re.findall(ppRgx, txt)

    byrRgx = "byr:([0-9]+)"
    iyrRgx = "iyr:([0-9]+)"
    eyrRgx = "eyr:([0-9]+)"
    hgtRgx = "hgt:([0-9]+cm|[0-9]+in)"
    hclRgx = "hcl:#([a-f0-9]+)"
    eclRgx = "ecl:([a-z]+)"
    pidRgx = "pid:([0-9]+)"

    validCount = 0
    trueValidCount = 0
    for passport in ppList:
        byrMatch = re.search(byrRgx, passport)
        iyrMatch = re.search(iyrRgx, passport)
        eyrMatch = re.search(eyrRgx, passport)
        hgtMatch = re.search(hgtRgx, passport)
        hclMatch = re.search(hclRgx, passport)
        eclMatch = re.search(eclRgx, passport)
        pidMatch = re.search(pidRgx, passport)
        if byrMatch and iyrMatch and eyrMatch and hgtMatch and hclMatch and eclMatch and pidMatch:
            byr = int(byrMatch.group(1))
            iyr = int(iyrMatch.group(1))
            eyr = int(eyrMatch.group(1))
            hgt = hgtMatch.group(1)
            hcl = hclMatch.group(1)
            ecl = eclMatch.group(1)
            pid = pidMatch.group(1)
            cmRgx = "([0-9]+)cm"
            inRgx = "([0-9]+)in"
            hgtRaw = 0
            cmMatch = re.search(cmRgx, hgt)
            hgtValid = False
            if cmMatch:
                hgtRaw = int(cmMatch.group(1))
                if hgtRaw >= 150 and hgtRaw <= 193:
                    hgtValid = True
            else:
                inMatch = re.search(inRgx, hgt)
                hgtRaw = int(inMatch.group(1))
                if hgtRaw >= 59 and hgtRaw <=76:
                    hgtValid = True
            eclValid = False
            if ecl == "amb" or ecl == "blu" or ecl == "brn" or ecl == "gry" or ecl == "grn" or ecl == "hzl" or ecl == "oth":
                eclValid = True
            if byr >= 1920 and byr <= 2002 and iyr >= 2010 and iyr <= 2020 and eyr >= 2020 and eyr <= 2030 and len(pid) == 9 and eclValid and hgtValid:
                validCount = validCount + 1

    print(validCount)