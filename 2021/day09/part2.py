#!/usr/bin/env python
import itertools
import math

with open('input.txt') as f:
    data = f.read().splitlines()

def get_nearby(data, x, y):
    nearby = []

    # Check Left
    if x > 0:
        if data[y][x-1] != '9':
            nearby.append((x - 1, y))
    # Check Right
    if x < len(data[0]) - 1:
        if data[y][x+1] != '9':
            nearby.append((x + 1, y))
    # Check Up
    if y > 0:
        if data[y-1][x] != '9':
            nearby.append((x, y - 1))
    # Check Down
    if y < len(data) - 1:
        if data[y+1][x] != '9':
            nearby.append((x, y + 1))

    return nearby


basins = []
for y in range(len(data)):
    for x in range(len(data[0])):
        # Skip 9 height
        if data[y][x] == '9':
            continue

        # Check if point is in existing basin
        if (x, y) in itertools.chain(*basins):
            continue

        checked = set()
        checked.add((x, y))

        nearby = get_nearby(data, x, y)

        while True:
            for n in nearby:
                if (n[0], n[1]) not in checked:
                    nearby += get_nearby(data, n[0], n[1])
                    checked.add((n[0], n[1]))
            else:
                basins.append(sorted(checked))
                break

print(math.prod(sorted(([len(x) for x in basins]))[-3:]))
