#!/usr/bin/python3

passports = []

with open('day04_data.txt', 'r') as inFile:
    currPassport = {}

    for inLine in inFile:
        inLine = inLine.rstrip()
        
        if inLine == "":
            passports.append(currPassport)
            currPassport = {}
        else:
            lineParts = inLine.split(" ")
            for part in lineParts:
                element = part.split(":")
                currPassport[element[0]] = element[1]

validCount = 0

for passport in passports:
    if ('byr' in passport.keys() and 'iyr' in passport.keys() and 'eyr' in passport.keys() and 'hgt' in passport.keys() and 'hcl' in passport.keys() and 'ecl' in passport.keys() and 'pid' in passport.keys() ):
        validCount += 1

print(validCount)
