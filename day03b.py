#!/usr/bin/python3

import numpy

treeMap = []
collisionCounts = []

with open('day03_data.txt', 'r') as inFile:
    for inLine in inFile:
        inLine = inLine.rstrip()

        mapLine = []
        for c in inLine:
            mapLine.append(c)

        treeMap.append(mapLine)

moveRules = [
    {'row': 1, 'col': 1},
    {'row': 1, 'col': 3},
    {'row': 1, 'col': 5},
    {'row': 1, 'col': 7},
    {'row': 2, 'col': 1}
    ]
   
for rule in moveRules:
    collisionCount = 0
    currLocation = {'row': 0, 'col': 0}

    while currLocation['row'] <= len(treeMap) - 1:
        if (currLocation['col'] > len(treeMap[0]) - 1): 
            currLocation['col'] -= len(treeMap[0])

        if (treeMap[currLocation['row']][currLocation['col']] == "#"):
            collisionCount += 1
        
        currLocation['row'] += rule['row'] 
        currLocation['col'] += rule['col']

    print(collisionCount)
    collisionCounts.append(collisionCount)

print(numpy.prod(collisionCounts))

