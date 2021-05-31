#!/usr/bin/python3

treeMap = []
collisionCount = 0

with open('day03_data.txt', 'r') as inFile:
    for inLine in inFile:
        inLine = inLine.rstrip()

        mapLine = []
        for c in inLine:
            mapLine.append(c)

        treeMap.append(mapLine)

rowRule = 1
colRule = 3
rowCurr = 0
colCurr = 0

while rowCurr <= len(treeMap) - 1:
    print (rowCurr, colCurr)
    if (colCurr > len(treeMap[0]) - 1): 
        colCurr -= len(treeMap[0])

    if (treeMap[rowCurr][colCurr] == "#"):
        collisionCount += 1
        treeMap[rowCurr][colCurr] = "X"
    else:
        treeMap[rowCurr][colCurr] = "O"
    
    rowCurr += rowRule
    colCurr += colRule

for row in treeMap:
    print(row)

print(collisionCount)
