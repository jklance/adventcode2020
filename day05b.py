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

seatIDs.sort()
print(seatIDs)
print(max(seatIDs))

mySeat = 0
prevSeat = 0

for seat in seatIDs:
    if prevSeat == 0:
        print("_")
    elif prevSeat + 1 != seat:
        print("*")
        mySeat = prevSeat + 1   

    prevSeat = seat

print(mySeat)
