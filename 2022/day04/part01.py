#!/usr/bin/env python

with open('day04.txt') as f:
    data = f.read().splitlines()

count = 0
for line in data:
    first = line.split(',')[0]
    second = line.split(',')[1]
    # We can probably determine this by the number itself, but going to make lists because I can
    first_range = list(range(int(first.split('-')[0]), int(first.split('-')[1]) + 1))
    second_range = list(range(int(second.split('-')[0]), int(second.split('-')[1]) + 1))

    # Check if things are subsets/supersets
    if set(first_range).issubset(set(second_range)) or set(first_range).issuperset(set(second_range)):
        count += 1

print(count)
