#!/usr/bin/env python
from itertools import product


def validate(boarding_pass):
    min_row = 0
    max_row = 127
    min_col = 0
    max_col = 7
    for x in boarding_pass[:7]:
        # Take Lower Half
        if x == 'F':
            max_row = int(max_row - ((max_row - min_row) / 2))
        # Take Upper Half
        else:
            min_row = max_row - (max_row - min_row) // 2
    for x in boarding_pass[7:]:
        # Take Lower Half
        if x == 'L':
            max_col = int(max_col - ((max_col - min_col) / 2))
        # Take Upper Half
        else:
            min_col = max_col - (max_col - min_col) // 2
    return max_row * 8 + max_col

def day5part1():
    max_pass = 0
    with open('day5.txt') as f:
        for line in f:
            line = line.strip()
            if validate(line) > max_pass:
                max_pass = validate(line)
    return max_pass

def day5part2():
    data = []
    with open('day5.txt') as f:
        for line in f:
            line = line.strip()
            data.append(validate(line))
    for x in product(['B', 'F'], repeat=7):
        for y in product(['L', 'R'], repeat=3):
            boarding_pass = ''.join(x) + ''.join(y)
            valid = validate(boarding_pass)
            if (valid + 1) in data and (valid - 1) in data and valid not in data:
                print(validate(boarding_pass))
    return

if __name__=="__main__":
    print(validate('FBFBBFFRLR'))
    print(validate('BFFFBBFRRR'))
    print(validate('FFFBBBFRRR'))
    print(validate('BBFFBBFRLL'))
    print(day5part1())
    day5part2()
