import numpy as np

array = np.genfromtxt('data3.txt', dtype=None, delimiter=31, comments=None, encoding=None)
# array = np.genfromtxt('data3-test.txt', dtype=None, delimiter=31, comments=None, encoding=None)

# print(len(array))
# print(len(array[0]))

# column = 0
# count = 0
# column_increment = 3

width = len(array[0])
height = len(array)


def calculate_trees(column_increment, height_increment):
    column = 0
    count = 0
    for row in range(1, height, height_increment):
        if column + column_increment >= width:
            column = column_increment - (width - column)
        else:
            column += column_increment

        if row >= height:
            break

        # print(f"Checking [{row}][{column}]")
        # print(array[row][column])

        if array[row][column] == '#':
            count += 1
    return count


slope1 = calculate_trees(1, 1)
print('Tree count 1 = ' + str(slope1))

slope2 = calculate_trees(3, 1)
print('Tree count 2 = ' + str(slope2))

slope3 = calculate_trees(5, 1)
print('Tree count 3 = ' + str(slope3))

slope4 = calculate_trees(7, 1)
print('Tree count 4 = ' + str(slope4))

# slope5 = calculate_trees(1, 2)
# print('Tree count 5 = ' + str(slope5))

#Right 1, down 2.
count = 0
line = 0
y = -1
ground = []
with open('data3.txt', 'r') as file:
  for i in file:
    line +=1
    if (line-1)%2 == 0:
      y += 1
      if i[y%31] == '#':
        count += 1

slope5 = count

print("Answer = " + str(slope1 * slope2 * slope3 * slope4 * slope5))


print(count)
print(str(slope1 * slope2 * slope3 * slope4 * count))