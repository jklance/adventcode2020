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

            currCount = 0
            for i in currPassword:
                if i == currRule:
                    currCount = currCount + 1

            if currCount < int(currThreshold[0]) or currCount > int(currThreshold[1]):
                invalidPasswords = invalidPasswords + 1
            else:
                validPasswords = validPasswords + 1
                print(currThreshold, currRule, currPassword)

print(validPasswords)
print(invalidPasswords)


