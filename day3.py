import numpy as np

array = np.genfromtxt('data3.txt', dtype=None, delimiter=31, comments=None, encoding=None)
# array = np.genfromtxt('data3-test.txt', dtype=None,delimiter=31, comments=None, encoding=None)

# print(len(array))
# print(len(array[0]))

column = 0
count = 0
column_increment = 3

width = len(array[0])
height = len(array)

for row in range(1, height):
    if column + column_increment >= width:
        column = column_increment - (width - column)
    else:
        column += 3

    print(f"Checking [{row}][{column}]")
    print(array[row][column])

    if array[row][column] == '#':
        count += 1

print('\nTree count = ' + str(count))
