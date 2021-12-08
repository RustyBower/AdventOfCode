#!/usr/bin/env python
import math
import statistics

with open('day7.txt') as f:
    data = f.read().strip()

crabs = list(map(int, data.split(',')))
min_crab = min(crabs)
max_crab = max(crabs)
#print(crabs, min_crab, max_crab)

fuel = []
#for num in range(min_crab, max_crab):
for num in [math.floor(statistics.mean(crabs)), math.ceil(statistics.mean(crabs))]:
    #print(num)
    #print([sum(range(0, abs(num - crab) + 1)) for crab in crabs])
    fuel.append(sum([sum(range(0, abs(num - crab) + 1)) for crab in crabs]))
    #print()

print(min(fuel))

#print(int(sum([abs(crab - median) for crab in crabs])))
