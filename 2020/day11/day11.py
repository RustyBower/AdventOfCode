#!/usr/bin/env python
import copy
import itertools

def calculate(data, x, y):
    x_range = [a for a in range(x-1, x+2) if a >= 0 if a < len(data[y])]
    y_range = [b for b in range(y-1, y+2) if b >= 0 if b < len(data)]
    adjacent_seats = list(itertools.product(x_range, y_range))
    # Remove Current Seat
    adjacent_seats.remove((x, y))


    # Calculate occupied seats around current seat
    occupied = 0
    for seat in adjacent_seats:
        # Skip if floor
        if data[seat[1]][seat[0]] == '#':
            occupied += 1
    return occupied

if __name__=="__main__":
    with open('day11.txt') as f:
        data = [data.strip() for data in f.readlines()]
        updated = copy.deepcopy(data)
        while True:
            seat_delta = 0
            for y, row in enumerate(data):
                for x, col in enumerate(row):
                    occupied = calculate(data, x, y)
                    # Skip if floor
                    if data[y][x] == '.':
                        continue
                    # Fill if empty and no seats adjacent
                    if data[y][x] == 'L' and occupied == 0:
                        seat_delta +=1
                        line = list(data[y])
                        line[x] = '#'
                        tmp_list = list(updated[y])
                        tmp_list[x] = '#'
                        updated[y] = ''.join(tmp_list)
                        continue
                    # Empty if 4 or more seats adjacent are full
                    if data[y][x] == '#' and occupied >= 4:
                        seat_delta += 1
                        line = list(data[y])
                        line[x] = 'L'
                        tmp_list = list(updated[y])
                        tmp_list[x] = 'L'
                        updated[y] = ''.join(tmp_list)
                        continue
            print('-' * 10)
            for row in updated:
                print(row)

            if seat_delta == 0:
                break

            data = copy.deepcopy(updated)
        print(list(''.join(data)).count('#'))
