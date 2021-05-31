#!/usr/bin/python

formsList = []
formsCounts = []

with open('day06_data.txt', 'r') as inFile:
    formLine = {}

    for inLine in inFile:
        inLine = inLine.rstrip()

        if inLine:
            for x in inLine:
                if x in formLine.keys() and formLine[x] == 1:
                    formLine[x] += 1
                else:
                    formLine[x] = 1
        else:
            formsList.append(formLine)
            formsCounts.append(len(formLine))
            formLine.clear()

print(sum(formsCounts))
