#!/usr/bin/python3

with open('day01_data.txt', 'r') as inFile:

    numList = []

    for inLine in inFile:
        inLine = inLine.rstrip()
        
        if inLine:
            numList.append(int(inLine))

for i in range(0,len(numList) - 1):
    for j in range(i + 1, len(numList)):
        numSum = numList[i] + numList[j]
        
        if numSum == 2020:
            numProd = numList[i] * numList[j]
            print (numList[i], numList[j], numProd)
            break
