#!/usr/bin/python

formsList = []
formsCounts = []

with open('day06_data.txt', 'r') as inFile:
    formLine = {}
    lineCount = 0

    for inLine in inFile:
        inLine = inLine.rstrip()

        if inLine:
            lineCount += 1
            for x in inLine:
                if x in formLine.keys():
                    formLine[x] += 1
                else:
                    formLine[x] = 1
        else:
            for x in formLine.keys():
                if formLine[x] != lineCount:
                    del formLine[x]

            formsList.append(formLine)
            formsCounts.append(len(formLine))
            formLine.clear()
            lineCount = 0

print(sum(formsCounts))
