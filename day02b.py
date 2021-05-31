#!/usr/bin/python3

invalidPasswords = validPasswords = 0

with open('day02_data.txt', 'r') as inFile:

    for inLine in inFile:
        inLine = inLine.rstrip()

        if inLine:
            lineParts = inLine.split(" ")
            currThreshold = lineParts[0].split("-")
            currRule = lineParts[1][0]
            currPassword = lineParts[2].rstrip()

            firstPos = currPassword[int(currThreshold[0]) - 1]
            secondPos = currPassword[int(currThreshold[1]) - 1]

            if ((firstPos == currRule or secondPos == currRule) and (firstPos != secondPos)):
                validPasswords = validPasswords + 1
                print(currThreshold, currRule, currPassword)
            else:
                invalidPasswords = invalidPasswords + 1

print(validPasswords)
print(invalidPasswords)


