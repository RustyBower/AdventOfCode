#!/usr/bin/env python
from collections import defaultdict
from itertools import accumulate

dir_size = defaultdict(int)
current_dir = []

with open('day07.txt') as f:
    data = f.read().splitlines()

for line in data:
    # Check if we have a command or output
    if line[0] == '$':
        # Change Directory
        if line.split()[1] == 'cd':
            if line.split()[2] == '..':
                current_dir.pop()
            else:
                current_dir.append(line.split()[2])
    # Otherwise it's output
    else:
        # There's a nested dir
        if line.split()[0] == 'dir':
            pass
        # Otherwise, it's a file and size
        else:
            size, filename = line.split()
            print(current_dir, filename, size)
            for x in accumulate(current_dir):
                print(x)
                dir_size[x] += int(size)

print(dir_size)
print(min([x for x in dir_size.values() if x > 8381165]))
