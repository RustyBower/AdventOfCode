#!/usr/bin/env python

with open('day5.txt') as f:
    data = f.read().splitlines()

size = 1000

grid = [['.' for x in range(size)] for y in range(size)]

for d in data:
    line = d.split(' -> ')

    x1, y1 = line[0].split(',')
    x2, y2 = line[1].split(',')

    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)

    # Vertical or Horizontal
    if x1 == x2 or y1 == y2:
        if x1 < x2:
            for x in range(x1, x2 + 1, 1):
                if y1 < y2:
                    for y in range(y1, y2 + 1, 1):
                        if grid[y][x] == '.':
                            grid[y][x] = 1
                        else:
                            grid[y][x] += 1
                else:
                    for y in range(y1, y2 - 1, -1):
                        if grid[y][x] == '.':
                            grid[y][x] = 1
                        else:
                            grid[y][x] += 1
        else:
            for x in range(x1, x2 - 1, -1):
                if y1 < y2:
                    for y in range(y1, y2 + 1, 1):
                        if grid[y][x] == '.':
                            grid[y][x] = 1
                        else:
                            grid[y][x] += 1
                else:
                    for y in range(y1, y2 - 1, -1):
                        if grid[y][x] == '.':
                            grid[y][x] = 1
                        else:
                            grid[y][x] += 1

    # Diagonal
    if x1 != x2 and y1 != y2:
        if x1 < x2 and y1 < y2:
            for x, y in zip(range(x1, x2 + 1), range(y1, y2 + 1)):
                    if grid[y][x] == '.':
                        grid[y][x] = 1
                    else:
                        grid[y][x] += 1
        if x1 < x2 and y1 > y2:
            for x, y in zip(range(x1, x2 + 1), range(y1, y2 - 1, -1)):
                    if grid[y][x] == '.':
                        grid[y][x] = 1
                    else:
                        grid[y][x] += 1
        if x1 > x2 and y1 < y2:
            for x, y in zip(range(x1, x2 - 1, -1), range(y1, y2 + 1)):
                    if grid[y][x] == '.':
                        grid[y][x] = 1
                    else:
                        grid[y][x] += 1
        if x1 > x2 and y1 > y2:
            for x, y in zip(range(x1, x2 - 1, -1), range(y1, y2 - 1, -1)):
                    if grid[y][x] == '.':
                        grid[y][x] = 1
                    else:
                        grid[y][x] += 1
count = 0
for row in grid:
    # print(''.join(map(str, row)))
    for col in row:
        if isinstance(col, int) and col > 1:
            count += 1
print(count)
