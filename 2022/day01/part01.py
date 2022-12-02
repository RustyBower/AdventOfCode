#!/usr/bin/env python
with open('day01.txt') as f:
    data = f.read()

max_cals = 0
elves = data.split('\n\n')
for elf in elves:
    cals = sum([int(x) for x in elf.split('\n') if x])
    if cals > max_cals:
        max_cals = cals
print(max_cals)
