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

snake = [[rows//2, cols//2] for x in range(10)]
#snake = [[0, 0] for x in range(11)]
start = [snake[0][0], snake[0][1]]

# Set start position
grid[snake[0][0]][snake[0][1]] = 'H'
visited[snake[-1][0]][snake[-1][1]] = 1

print('== Initial State ==')
print()
print_grid(grid)

for command in data:
    print()
    print('== ' + command + ' ==')
    print()
    
    direction = command.split()[0]
    distance = int(command.split()[1])

    for x in range(distance, 0, -1):
        # Clear head from map
        grid = np.full((rows, cols), '.')

        if direction == 'R':
            snake[0][0] += 1
        if direction == 'L':
            snake[0][0] -= 1
        if direction == 'U':
            snake[0][1] -= 1
        if direction == 'D':
            snake[0][1] += 1

        for x in range(1, len(snake)):
            # Check if tail is too far away
            if abs(snake[x][0] - snake[x-1][0]) >= 1 and abs(snake[x][1] - snake[x-1][1]) > 1:
                    if snake[x-1][0] > snake[x][0]:
                        snake[x][0] += 1
                    else:
                        snake[x][0] -= 1
                    if snake[x-1][1] > snake[x][1]:
                        snake[x][1] += 1
                    else:
                        snake[x][1] -= 1
            if abs(snake[x][0] - snake[x-1][0]) > 1 and abs(snake[x][1] - snake[x-1][1]) >= 1:
                    if snake[x-1][0] > snake[x][0]:
                        snake[x][0] += 1
                    else:
                        snake[x][0] -= 1
                    if snake[x-1][1] > snake[x][1]:
                        snake[x][1] += 1
                    else:
                        snake[x][1] -= 1
            # These work if the head only moved laterally
            elif abs(snake[x][0] - snake[x-1][0]) > 1:
                if snake[x-1][0] > snake[x][0]:
                    snake[x][0] += 1
                else:
                    snake[x][0] -= 1
            elif abs(snake[x][1] - snake[x-1][1]) > 1:
                if snake[x-1][1] > snake[x][1]:
                    snake[x][1] += 1
                else:
                    snake[x][1] -= 1

            # Update visited
            visited[snake[-1][1]][snake[-1][0]] = 1

        # Update map
        grid[start[1]][start[0]] = 's'
        for x in range(len(snake), 0, -1):
            if x-1 == 0: 
                grid[snake[x-1][1], snake[x-1][0]] = 'H'
            #elif x == len(snake):
                #grid[snake[x-1][1], snake[x-1][0]] = 'T'
            else:
                grid[snake[x-1][1], snake[x-1][0]] = x-1

    #print_grid(grid)

print()
print(visited)
print(visited.sum())
