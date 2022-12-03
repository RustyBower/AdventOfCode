#!/usr/bin/env python

badges = 0
with open('day03.txt') as f:
    data = f.read().splitlines()

for x in range(0, len(data), 3):
    a = data[x]
    b = data[x+1]
    c = data[x+2]

    # Assuming just a single letter for badge
    badge = list(set(a) & set(b) & set(c))[0]

    if badge.islower():
        badges += ord(badge) - 96
    else:
        badges += ord(badge) - 38

print(badges)
