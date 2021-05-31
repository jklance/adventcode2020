#!/usr/bin/python3

import re

def isBYRValid(passport):
    if ('byr' in passport.keys()):
        year = int(passport['byr'])
        if (year >= 1920 and year <= 2002):
            return True

    print('byr')
    return False

def isIYRValid(passport):
    if ('iyr' in passport.keys()):
        year = int(passport['iyr'])
        if (year >= 2010 and year <= 2020):
            return True

    print('iyr')
    return False

def isEYRValid(passport):
    if ('eyr' in passport.keys()):
        year = int(passport['eyr'])
        if (year >= 2020 and year <= 2030):
            return True

    print('eyr')
    return False

def isHGTValid(passport):
    if ('hgt' in passport.keys()):
        hgt = int(passport['hgt'][:-2])
        unit = passport['hgt'][-2:]

        if (unit == 'cm' and hgt >= 150 and hgt <= 193):
            return True
        
        if (unit == 'in' and hgt >= 59 and hgt <= 76):
            return True        

    print('hgt')
    return False

def isHCLValid(passport):
    if ('hcl' in passport.keys()):
        if (re.match('^#([0-9A-Fa-f]{6})$', passport['hcl'])): 
            return True

    print('hcl')
    return False

def isECLValid(passport):
    if ('ecl' in passport.keys()):
        if (passport['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth']):
            return True

    print('ecl')
    return False

def isPIDValid(passport):
    if ('pid' in passport.keys()):
        if (re.match('^[0-9]{9}$', passport['pid'])):
            return True

    print('pid')
    return False

def isPassportValid(passport):
    if (isBYRValid(passport) and isIYRValid(passport) and isEYRValid(passport) and isHGTValid(passport) and isHCLValid(passport) and isECLValid(passport) and isPIDValid(passport)):
        return True
    return False

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
    if (isPassportValid(passport)):
        validCount += 1
        print('valid', passport)
    else:
        print('invalid',passport)

print(validCount)
