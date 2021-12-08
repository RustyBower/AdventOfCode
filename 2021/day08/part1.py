#!/usr/bin/env python

with open('input.txt') as f:
    data = f.read().splitlines()

count = 0
for row in data:
    i = row.split(' | ')[0]
    output = row.split(' | ')[1]

    count += len([x for x in output.split() if len(x) in [2, 3, 4, 7]])
print(count)
