#!/usr/bin/env python

priorities = 0
with open('day03.txt') as f:
    for line in f:
        line = line.strip()
        first = line[:int(len(line)/2)]
        second = line[int(len(line)/2):]

        # Assuming just a single letter for priority
        priority = list(set(first) & set(second))[0]

        if priority.islower():
            priorities += ord(priority) - 96
        else:
            priorities += ord(priority) - 38

print(priorities)
