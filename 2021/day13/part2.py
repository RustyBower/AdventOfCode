#!/usr/bin/env python
import numpy as np

def fold(paper, axis, offset):
    shape = list(paper.shape)
    if axis == 'y':
        shape[0] = offset
    elif axis == 'x':
        shape[1] = offset
    for y, row in enumerate(paper):
        for x, col in enumerate(row):
            if col == '#':
                if axis == 'y':
                    if y > offset:
                        paper[y - (2 * (y - offset))][x] = '#'
                elif axis == 'x':
                    if x > offset:
                        #print(y, x, offset)
                        #print(y, x - (2 * (x - offset)))
                        paper[y][x - (2 * (x - offset))] = '#'
    return paper[:shape[0], :shape[1]]


with open('input') as f:
    data = f.read().splitlines()

points = [tuple(map(int, point.split(','))) for point in data[:data.index('')]]
folds = data[data.index('') + 1:]

paper = np.full((2000, 2000), '.')

for x, y in points:
    paper[int(y)][int(x)] = '#'

'''
print(paper)
for i in paper:
    print(''.join(map(str, i)))
paper = fold(paper, 'y', 7)
print()
#print(paper)
for i in paper:
    print(''.join(map(str, i)))
print()
paper = fold(paper, 'x', 5)
#print(paper)
for i in paper:
    print(''.join(map(str, i)))
'''
for i in paper:
    print(''.join(map(str, i)))

for f in folds:
    f = f.split('=')
    axis = f[0].split()[-1]
    offset = int(f[1])
    #print(paper)
    #print(np.count_nonzero(paper == '#'))
    paper = fold(paper, axis, offset)
    #print(paper)
    #print(np.count_nonzero(paper == '#'))
    for i in paper:
        print(''.join(map(str, i)))
    print()
