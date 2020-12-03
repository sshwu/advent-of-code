import re

def runDayThree():
    f = open("input3.txt","r")
    txt = f.read()
    rgx = "[\.#]+"
    grid = re.findall(rgx, txt)
    rows = len(grid)
    columns = len(grid[0])
    r = 1
    c1 = 1
    c2 = 3
    c3 = 5
    c4 = 7
    c5 = 1
    treeCount1 = 0
    treeCount2 = 0
    treeCount3 = 0
    treeCount4 = 0
    treeCount5 = 0
    while r < rows:
        if grid[r][c1] == "#":
            treeCount1 = treeCount1 + 1
        if grid[r][c2] == "#":
            treeCount2 = treeCount2 + 1
        if grid[r][c3] == "#":
            treeCount3 = treeCount3 + 1
        if grid[r][c4] == "#":
            treeCount4 = treeCount4 + 1
        if r % 2 == 0 and grid[r][c5] == "#":
            treeCount5 = treeCount5 + 1
        if r % 2 == 0:
            c5 = c5 + 1
        r = r + 1
        c1 = c1 + 1
        c2 = c2 + 3
        c3 = c3 + 5
        c4 = c4 + 7
        
        if c1 >= columns:
            c1 = c1 - columns
        if c2 >= columns:
            c2 = c2 - columns
        if c3 >= columns:
            c3 = c3 - columns
        if c4 >= columns:
            c4 = c4 - columns
        if c5 >= columns:
            c5 = c5 - columns
    print(treeCount2)
    print(treeCount1 * treeCount2 * treeCount3 * treeCount4 * treeCount5)