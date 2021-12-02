#!/usr/bin/env python

with open('day2.txt') as f:
    data = f.read().splitlines()

pos, depth, aim = 0, 0, 0
for x in data:
    command = x.split()[0]
    units = x.split()[1]

    if command == 'forward':
        pos += int(units)
        depth += (int(units) * aim)

    if command == 'up':
        aim -= int(units)
    if command == 'down':
        aim += int(units)

print(pos, depth, pos * depth)
