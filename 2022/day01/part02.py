#!/usr/bin/env python
with open('day01.txt') as f:
    data = f.read()

sums = []
elves = data.split('\n\n')
for elf in elves:
    sums.append(sum([int(x) for x in elf.split('\n') if x]))
print(sum(sorted(sums, reverse=True)[:3]))
