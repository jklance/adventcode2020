#!/usr/bin/python

boardingPasses = []

with open('day05_data.txt', 'r') as inFile:
    for inLine in inFile:
        boardingPasses.append(inLine.rstrip())

seatIDs = []

for boardingPass in boardingPasses:
    planeB  = 127
    planeF  = 0
    planeR  = 7
    planeL  = 0

    for x in boardingPass:
        if x == 'B':
            planeF += (((planeB - planeF) + 1) / 2)   
        if x == 'F':
            planeB -= (((planeB - planeF) + 1) / 2)
        if x == 'L':
            planeR -= (((planeR - planeL) + 1) / 2)
        if x == 'R':
            planeL += (((planeR - planeL) + 1) / 2)

    seatIDs.append((planeB * 8) + planeR)

print(seatIDs)
print(max(seatIDs))



