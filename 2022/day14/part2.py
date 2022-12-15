#!/usr/bin/env python
import numpy as np

np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=np.inf)


def print_grid(grid):
    top = min(np.where(grid == '#')[0])
    bottom = max(np.where(grid == '#')[0])
    left = min(np.where(grid == '#')[1])
    right = max(np.where(grid == '#')[1])
    for y in grid[0:bottom + 2]:
        #print(''.join(y[left-1:right+1]))
        print(''.join(y[400:600]))
    #print(grid[0:bottom+1, left-1:right+1])

#def sand(start, grid, left, right):
def sand(start, grid):
    y, x = int(start[0]), int(start[1])
    #if x < left or x > right:
    #print(x, y)
    #print(grid[:10,494:504])

    # Reset where we came from
    #if np.where(grid == '+') != (y, x):
        #grid[y][x] = '.'

    # Check
    if grid[y+1][x] == '.':
        #grid[y+1][x] = 'o'
        return sand((y+1, x), grid)
    elif grid[y+1][x-1] == '.':
        #grid[y+1][x-1] = 'o'
        return sand((y+1, x-1), grid)
    elif grid[y+1][x+1] == '.':
        #grid[y+1][x+1] = 'o'
        return sand((y+1, x+1), grid)
    else:
        grid[y][x] = 'o'
        if y == 0 and x == 500:
            print("WE'RE AT THE SOURCE")
            return False
        #print("We've come to rest")
        return True
    return

with open('input.txt') as f:
    data = f.read().splitlines()

grid = np.full((1000,1000), '.')
grid[0][500] = '+' # sand source
for line in data:
    points = [x.split(',') for x in  line.split(' -> ')]
    for x in range(len(points) - 1):
        #print(points[x], points[x+1])
        start_x, start_y = points[x]
        end_x, end_y = points[x+1]
        # I hate this
        start_x, start_y, end_x, end_y = int(start_x), int(start_y), int(end_x), int(end_y)
        #print(start_x, start_y)
        # Go horizontal
        if start_y == end_y:
            if start_x < end_x:
                for x0 in range(start_x, end_x + 1):
                    #print(x0)
                    grid[start_y][x0] = '#'
            else:
                for x0 in range(end_x, start_x + 1):
                    #print(x0)
                    grid[start_y][x0] = '#'
        elif start_x == end_x:
            if start_y < end_y:
                for y0 in range(start_y, end_y + 1):
                    #print(y0)
                    grid[y0][start_x] = '#'
            else:
                for y0 in range(end_y, start_y + 1):
                    #print(y0)
                    grid[y0][start_x] = '#'
        else:
            print("Something else")
    #print('-' * 10)

bottom = max(np.where(grid == '#')[0])
print(bottom)
grid[bottom+2] = '#'
print_grid(grid)
print()
start = np.where(grid == '+')

count = 1
while True:
    if not sand(start, grid):
        break
    '''
    print(f"== {count} ==")
    print_grid(grid)
    count += 1
    print()
    '''

print_grid(grid)
unique, counts = np.unique(grid, return_counts=True)
print(unique, counts)
