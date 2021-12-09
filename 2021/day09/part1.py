#!/usr/bin/env python

with open('input.txt') as f:
    data = f.read().splitlines()

low_points = []
for y in range(len(data)):
    for x in range(len(data[0])):
        nearby = []
        #print(data[y][x])
        # Check Left
        if x > 0:
            nearby.append(data[y][x-1])
        # Check Right
        if x < len(data[0]) - 1:
            nearby.append(data[y][x+1])
        # Check Up
        if y > 0:
            nearby.append(data[y-1][x])
        # Check Down
        if y < len(data) - 1:
            nearby.append(data[y+1][x])

        if data[y][x] < min(nearby):
            #print(data[y][x], nearby)
            low_points.append(data[y][x])

risk_level = [int(x) + 1 for x in low_points]
print(sum(risk_level))
