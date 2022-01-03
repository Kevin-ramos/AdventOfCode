import re
import numpy as np

def part_1(input):
    with open(input, 'r') as f:
        lines = f.readlines()
        lines = [entry.strip() for entry in lines]
    max_x = 0
    max_y = 0
    for line in lines:
        x1, y1, x2, y2 = [int(entry) for entry in re.sub('[^0-9]', ' ', line).split()]
        max_x = max(max_x, x1, x2)
        max_y = max(max_y, y1, y2)
    print("Puntos máximos: ")
    print('X: ', max_x, '\nY: ', max_y)
    field = np.zeros((max_y+1, max_x+1), dtype=int)
    for line in lines:
        x1, y1, x2, y2 = [int(entry) for entry in re.sub('[^0-9]', ' ', line).split()]
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                field[y, x1] += 1
        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                field[y1, x] += 1
    print('Total: ', (field >= 2).sum())
#part_1('input.txt')

def addValues(field, x1, y1, x2, y2):
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2)+1):
            field[y, x1] += 1
        return
    if y1 == y2:
        for x in range(min(x1, x2), max(x1, x2)+1):
            field[y1, x] += 1
        return
    line_length = abs(x1-x2)+1
    step_x = 1 if x2-x1 > 0 else -1
    step_y = 1 if y2-y1 > 0 else -1
    for i in range(line_length):
        new_x = x1 + i*step_x
        new_y = y1 + i*step_y
        field[new_y, new_x] += 1

def part_2(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        lines = [entry.strip() for entry in lines]

    max_x = 0
    max_y = 0
    for line in lines:
        x1, y1, x2, y2 = [int(entry) for entry in re.sub('[^0-9]', ' ', line).split()]
        max_x = max(max_x, x1, x2)
        max_y = max(max_y, y1, y2)

    print("Puntos máximos: ")
    print('X: ', max_x, '\nY: ', max_y)
    field = np.zeros((max_y+1, max_x+1), dtype=int)

    for line in lines:
        x1, y1, x2, y2 = [int(entry) for entry in re.sub('[^0-9]', ' ', line).split()]

        addValues(field, x1, y1, x2, y2)

    print('score', (field >= 2).sum())

part_2('input.txt')


