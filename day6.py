# for each line
#     for each char
#         add to a set
# if empty line
#     store count

running_count = 0
current_set = set()

with open('data6.txt') as f:
    for line, data in enumerate(f):

        if data == '\n':
            # print(current_set)
            running_count += len(current_set)
            current_set = set()
            continue

        # data = data.strip()
        # print(data)

        for char in data.strip():
            # print(char)
            current_set.add(char)

if data != '\n':
    running_count += len(current_set)

print(running_count)