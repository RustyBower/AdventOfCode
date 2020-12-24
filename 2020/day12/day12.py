#!/usr/bin/env python

def part1():
    with open('day12.txt') as f:
        direction = 90
        x, y = 0, 0
        for line in f:
            line = line.strip()
            action = line[0]
            value = int(line[1:])
            print(action, value)
            # Turn Left
            if action == 'L':
                direction -= value
                direction = direction % 360
            # Turn Right
            if action == 'R':
                direction += value
                direction = direction % 360

            # Move North
            if action == 'N':
                y += value
            # Move East
            if action == 'E':
                x += value
            # Move South
            if action == 'S':
                y -= value
            # Move West
            if action == 'W':
                x -= value

            # Move Forward
            if action == 'F':
                if direction == 0:
                    y += value
                if direction == 90:
                    x += value
                if direction == 180:
                    y -= value
                if direction == 270:
                    x -= value

            print(x, y, direction)
        print(abs(x - 0) + abs(y - 0))

if __name__=='__main__':
    part1()
