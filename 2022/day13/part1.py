#!/usr/bin/env python
from itertools import zip_longest as zip

def compare_indices(x, y, indent=0):
    print(f'Compare {x} vs {y}')

    if x is None:
        print('Left side ran out of items, so inputs are in the right order')
        return True

    if isinstance(x, (int, list)) and y is None:
        print('Right side ran out of items, so inputs are not in the right order')
        return False

    # If both ints
    if isinstance(x, int) and isinstance(y, int):
        # If left > right, wrong order
        if x < y:
            print('Left side is smaller, so inputs are in the right order')
            return True
        if x == y:
            return None
        if x > y:
            print('Right side is smaller, so inputs are not in the right order')
            return False

    # If both lists
    if isinstance(x, list) and isinstance(y, list):
        for x0, y0 in zip(x, y):
            print(x0, y0)
            res = compare_indices(x0, y0, indent)
            if res is True:
                return True
            if res is False:
                return False
        #return(any(compare_indices(x0, y0) for x0, y0 in zip(x, y)))

    # If one is int
    if isinstance(x, int) or isinstance(y, int):
        if isinstance(x, int):
            print(f'Mixed types; convert left to [{x}] and retry comparison')
            x0 = [x]
            y0 = y
        if isinstance(y, int):
            print(f'Mixed types; convert right to [{y}] and retry comparison')
            x0 = x
            y0 = [y]
        indent += 2
        return compare_indices(x0, y0, indent)

    print("Some weird combination of things")

with open('testinput.txt') as f:
#with open('input.txt') as f:
    data = [eval(x) for x in f.read().splitlines() if x]

indices = [None for _ in range(len(data) // 2)]
for i, v in enumerate(range(0, len(data), 2)):
    print(f'== Pair {i+1} ==')
    indices[i] = compare_indices(data[v], data[v+1])
    '''
    #print(i, data[v], data[v+1])
    for x, y in zip(data[v], data[v+1]):
        print(x, y)
        res = check_indices(x, y)
        if not res:
            indices[i] = res
            break
    '''
    print()

print(indices)
print(sum([i + 1 for i, v in enumerate(indices) if v is True]))
