passports = []
passport = {}
validCount = 0

with open('data4.txt') as f:
    for line, data in enumerate(f):
        # print(data)

        if data == '\n':
            passports.append(passport)
            passport = {}
            continue

        tokens = data.split()
        # print(tokens)
        for token in tokens:
            entry = token.split(':')
            passport[entry[0]] = entry[1]

if data != '\n':
    passports.append(passport)


# print(passports)


def checkKey(passportToCheck, param):
    return param in passportToCheck


def validate(passportToCheck):
    print(passportToCheck)
    compulsoryFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    for field in compulsoryFields:
        if not checkKey(passportToCheck, field):
            return False

    return True


for passport in passports:
    if validate(passport):
        validCount += 1

print(str(validCount) + ' valid passports')
