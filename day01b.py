#!/usr/bin/python3

with open('day01_data.txt', 'r') as inFile:

    numList = []

    for inLine in inFile:
        inLine = inLine.rstrip()
        
        if inLine:
            numList.append(int(inLine))

for i in range(0,len(numList) - 1):
    for j in range(i + 1, len(numList)):
        for k in range(j + 1, len(numList)):
            numSum = numList[i] + numList[j] + numList[k]
        
            if numSum == 2020:
                numProd = numList[i] * numList[j] * numList[k]
                print (numList[i], numList[j], numList[k], numProd)
                break
