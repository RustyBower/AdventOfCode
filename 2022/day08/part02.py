#!/usr/bin/env python
import math

def scenic_score(row, col, trees):
    up, down, left, right = 0, 0, 0, 0
    #print(row, col, trees, trees[row][col])

    # Check left
    for x in trees[row][:col][::-1]:
        left += 1
        if x >= trees[row][col]:
            break

    # Check right
    for x in trees[row][col+1:]:
        right += 1
        if x >= trees[row][col]:
            break

    # Check top
    # https://stackoverflow.com/questions/903853/how-do-you-extract-a-column-from-a-multi-dimensional-array
    for x in [y[col] for y in trees][:row][::-1]:
        up += 1
        if x >= trees[row][col]:
            break

    # Check bottom
    for x in [y[col] for y in trees][row+1:]:
        down += 1
        if x >= trees[row][col]:
            break

    return up, left, down, right


with open('day08.txt') as f:
#with open('testinput.txt') as f:
    data = f.read().splitlines()


scenic_scores = list()
for i, row in enumerate(data):
    # Exclude outermost ring
    if (i == 0) or (i == len(row) - 1):
        continue
    for j, col in enumerate(row):
        # Exclude outermost ring
        if (j == 0) or (j == len(row) - 1):
            continue
        scenic_scores.append((math.prod(scenic_score(i, j, data))))

print(max(scenic_scores))
