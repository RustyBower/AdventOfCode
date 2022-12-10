#!/usr/bin/env python

visible_trees = 0

def check_visible(row, col, trees):
    #print(row, col, trees, trees[row][col])

    # Check left
    if not any(x >= trees[row][col] for x in trees[row][:col]):
        return True

    # Check right
    if not any(x >= trees[row][col] for x in trees[row][col+1:]):
        return True

    # Check top
    # https://stackoverflow.com/questions/903853/how-do-you-extract-a-column-from-a-multi-dimensional-array
    if not any(x >= trees[row][col] for x in [y[col] for y in trees][:row]):
        return True

    # Check bottom
    if not any(x >= trees[row][col] for x in [y[col] for y in trees][row+1:]):
        return True

    return False


with open('day08.txt') as f:
    data = f.read().splitlines()


for i, row in enumerate(data):
    # Exclude outermost ring
    if (i == 0) or (i == len(row) - 1):
        visible_trees += len(row)
        continue
    for j, col in enumerate(row):
        # Exclude outermost ring
        if (j == 0) or (j == len(row) - 1):
            visible_trees += 1
            continue
        if check_visible(i, j, data):
            visible_trees += 1

print(visible_trees)
