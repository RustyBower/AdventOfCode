#!/usr/bin/env python

score = 0

with open('day02.txt') as f:
    for line in f.readlines():
        line = line.strip()
        shapes = line.split()

        # Rock
        if shapes[0] == 'A' and shapes[1] == 'X':
            score += 0
            score += 3 # Scissors
        if shapes[0] == 'A' and shapes[1] == 'Y':
            score += 3
            score += 1 # Rock
        if shapes[0] == 'A' and shapes[1] == 'Z':
            score += 6
            score += 2 # Paper

        # Paper
        if shapes[0] == 'B' and shapes[1] == 'X':
            score += 0
            score += 1 # Rock
        if shapes[0] == 'B' and shapes[1] == 'Y':
            score += 3
            score += 2 # Paper
        if shapes[0] == 'B' and shapes[1] == 'Z':
            score += 6
            score += 3 # Scissors

        # Scissors
        if shapes[0] == 'C' and shapes[1] == 'X':
            score += 0
            score += 2 # Paper
        if shapes[0] == 'C' and shapes[1] == 'Y':
            score += 3
            score += 3 # Scissors
        if shapes[0] == 'C' and shapes[1] == 'Z':
            score += 6
            score += 1 # Rock

print(score)
