import re

with open('data2.txt') as f:
    data = f.read().splitlines()

pattern = re.compile('^([\d]{1,2})-([\d]{1,2})\s([a-zA-Z])$')


def splitPolicy(policy):
    res = pattern.match(policy)

    return res.groups()


valid_ex1 = 0
valid_ex2 = 0

for line in data:
    split = line.split(':')
    min, max, char = splitPolicy(split[0])
    password = split[1]

    # print(f"Received {min}, {max}, {char}")

    charCount = password.count(char)
    # print(f"Found {charCount} occurrences of {char} in {password}")

    if int(min) <= charCount <= int(max):
        valid_ex1 += 1

    firstPos = int(min)
    secondPos = int(max)

    if secondPos > len(password) or firstPos > len(password):
        print("ERRRRRRRROOOOOOORRRRRRR")
    else:
        if (password[firstPos] == char and password[secondPos] != char) or (
                password[secondPos] == char and password[firstPos] != char):
            # print(f"Looking for {char} in {password}: Char at pos {firstPos} is {password[firstPos]} and pos {
            # secondPos} is {password[secondPos]}")
            valid_ex2 += 1

print("\n======")
print(str(valid_ex1) + " valid passwords for policy1")
print(str(valid_ex2) + " valid passwords for policy2")
