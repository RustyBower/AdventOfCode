#!/usr/bin/env python

with open('day1.txt') as f:
    data = f.read().splitlines() 


increased = 0
for i, value in enumerate(data):

    first = sum(map(int, data[i-1:i+2]))
    second = sum(map(int, data[i:i+3]))

    if i == 0:
        print(f"{second} (N/A - no previous sum)")
        continue

    if second > first:
        print(f"{second} (increased)")
        increased += 1
    elif second < first:
        print(f"{second} (decreased)")
    else:
        print(f"{second} (no change)")

print(increased)
