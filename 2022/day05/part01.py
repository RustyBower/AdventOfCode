#!/usr/bin/env python
from collections import deque

with open('day05.txt') as f:
    data = f.read().splitlines()

num_stacks = data[data.index('') - 1].split()[-1]
stack = [deque() for i in range(int(num_stacks))]

# Loop over starting stacks
for line in data:
    # Break on the box index
    if line[1] == '1':
        break

    #print(line)
    for i, v in enumerate(range(1, len(line), 4)):
        if line[v] != ' ':
            print(i, v, line[v])
            stack[i].appendleft(line[v])
    print('-' * 10)

print(stack)

moves = data[data.index('') + 1:]
for move in moves:
    print(move)
    num_boxes = int(move.split()[1])
    start = int(move.split()[3])
    end = int(move.split()[5])
    print(num_boxes, start, end)
    for _ in range(num_boxes):
        stack[end-1].append(stack[start-1].pop())
    print(stack)

print('-' * 10)
print(''.join([x[-1] for x in stack if x]))
