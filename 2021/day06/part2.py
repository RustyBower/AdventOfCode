#!/usr/bin/env python
import timeit
from collections import Counter

with open('day6.txt') as f:
    data = f.read().strip().split(',')

days = 256

'''
data = [int(x) for x in data]
print('Initial state:', ','.join(map(str, data)))
'''
counter = Counter([int(x) for x in data])
print(counter)

for d in range(1, days + 1):
    temp_counter = Counter()

    for x in range(8, -1, -1):
        temp_counter[x-1] = counter[x]

    temp_counter[6] += temp_counter[-1]
    temp_counter[8] += temp_counter[-1]
    temp_counter[-1] = 0

    counter = temp_counter

print(counter)
print(sum(counter.values()))
