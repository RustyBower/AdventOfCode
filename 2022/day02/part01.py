#!/usr/bin/env python

score = 0

with open('day02.txt') as f:
    for line in f.readlines():
        line = line.strip()
        shapes = line.split()

        # Add score for shape choice
        score += ord(shapes[1]) % 87

        # Rock
        if shapes[0] == 'A' and shapes[1] == 'X':
            score += 3
        if shapes[0] == 'A' and shapes[1] == 'Y':
            score += 6
        if shapes[0] == 'A' and shapes[1] == 'Z':
            score += 0

        # Paper
        if shapes[0] == 'B' and shapes[1] == 'X':
            score += 0
        if shapes[0] == 'B' and shapes[1] == 'Y':
            score += 3
        if shapes[0] == 'B' and shapes[1] == 'Z':
            score += 6

        # Scissors
        if shapes[0] == 'C' and shapes[1] == 'X':
            score += 6
        if shapes[0] == 'C' and shapes[1] == 'Y':
            score += 0
        if shapes[0] == 'C' and shapes[1] == 'Z':
            score += 3

print(score)
