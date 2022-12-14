#!/usr/bin/env python
from itertools import zip_longest as zip
from functools import cmp_to_key

def compare_indices(x, y):
    print(f'Compare {x} vs {y}')

    if x == y:
        return 0

    if x is None:
        #print('Left side ran out of items, so inputs are in the right order')
        return 1

    if isinstance(x, (int, list)) and y is None:
        #print('Right side ran out of items, so inputs are not in the right order')
        return -1

    # If both ints
    if isinstance(x, int) and isinstance(y, int):
        # If left > right, wrong order
        if x < y:
            #print('Left side is smaller, so inputs are in the right order')
            return 1
        if x == y:
            return None
        if x > y:
            #print('Right side is smaller, so inputs are not in the right order')
            return -1

    # If both lists
    if isinstance(x, list) and isinstance(y, list):
        for x0, y0 in zip(x, y):
            #print(x0, y0)
            res = compare_indices(x0, y0)
            if res is 1:
                return 1
            if res is -1:
                return -1 
        #return(any(compare_indices(x0, y0) for x0, y0 in zip(x, y)))

    # If one is int
    if isinstance(x, int) or isinstance(y, int):
        if isinstance(x, int):
            #print(f'Mixed types; convert left to [{x}] and retry comparison')
            x0 = [x]
            y0 = y
        if isinstance(y, int):
            #print(f'Mixed types; convert right to [{y}] and retry comparison')
            x0 = x
            y0 = [y]
        return compare_indices(x0, y0)

    print("Some weird combination of things")

with open('input.txt') as f:
#with open('input.txt') as f:
    data = [eval(x) for x in f.read().splitlines() if x]

data.append([[2]])
data.append([[6]])

packets = sorted(data, key=cmp_to_key(compare_indices), reverse=True)

print(packets)
print(packets.index([[2]]) + 1, packets.index([[6]]) + 1)
print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))
