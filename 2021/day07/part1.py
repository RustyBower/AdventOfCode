#!/usr/bin/env python
import statistics

with open('day7.txt') as f:
    data = f.read().strip()

crabs = list(map(int, data.split(',')))
median = statistics.median(crabs)

print(int(sum([abs(crab - median) for crab in crabs])))
