#!/usr/bin/env
import numpy as np

def print_grid(grid):
    for i in grid:
        print(''.join(map(str, i)))
    return

with open('day09.txt') as f:
    data = f.read().splitlines()

print(data)

rows, cols = 1000, 1000
grid = np.full((rows, cols), '.')
visited = np.zeros((rows, cols))

head = [rows//2, cols//2]
tail = [rows//2, cols//2]
start = [rows//2, cols//2]

# Set start position
grid[head[0]][head[1]] = 'H'
visited[tail[0]][tail[1]] = 1

print('== Initial State ==')
print()
print_grid(grid)

for command in data:
    #print()
    #print('== ' + command + ' ==')
    #print()
    
    direction = command.split()[0]
    distance = int(command.split()[1])

    for x in range(distance, 0, -1):
        #print(x)
        # Clear head from map
        grid = np.full((rows, cols), '.')

        if direction == 'R':
            head[0] += 1
        if direction == 'L':
            head[0] -= 1
        if direction == 'U':
            head[1] -= 1
        if direction == 'D':
            head[1] += 1

        # Check if tail is too far away
        if abs(tail[0] - head[0]) >= 1 and abs(tail[1] - head[1]) > 1:
                if head[0] > tail[0]:
                    tail[0] += 1
                else:
                    tail[0] -= 1
                if head[1] > tail[1]:
                    tail[1] += 1
                else:
                    tail[1] -= 1
        if abs(tail[0] - head[0]) > 1 and abs(tail[1] - head[1]) >= 1:
                if head[0] > tail[0]:
                    tail[0] += 1
                else:
                    tail[0] -= 1
                if head[1] > tail[1]:
                    tail[1] += 1
                else:
                    tail[1] -= 1
        # These work if the head only moved laterally
        elif abs(tail[0] - head[0]) > 1:
            if head[0] > tail[0]:
                tail[0] += 1
            else:
                tail[0] -= 1
        elif abs(tail[1] - head[1]) > 1:
            if head[1] > tail[1]:
                tail[1] += 1
            else:
                tail[1] -= 1

        # Update visited
        visited[tail[1]][tail[0]] = 1

        # Update map
        grid[start[1]][start[0]] = 's'
        grid[tail[1]][tail[0]] = 'T'
        grid[head[1]][head[0]] = 'H'

        #print_grid(grid)

print()
print(visited)
print(visited.sum())
