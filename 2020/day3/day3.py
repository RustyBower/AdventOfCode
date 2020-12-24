#!/usr/bin/env python

def parsemap(data, x_slope, y_slope):
    x, y = 0, 0
    count = 0
    iterdata = enumerate(data)
    for row, line in iterdata:
        line = line.strip()
        line = list(line)

        if row == 0:
            #print(''.join(line))
            continue

        if row % y_slope != 0:
            #print(''.join(line))
            continue

        x += x_slope

        if x >= len(line):
            line = line * int(((x / len(line)) + 1))
        if line[x] == '#':
            line[x] = 'X'
            count += 1
        else:
            line[x] = 'O'
        #print(''.join(line))
    return count

def day3test():
    with open('test.txt') as f:
        data = [x.strip() for x in f.readlines()]
        print(parsemap(data, 3, 1))

def day3part1():
    with open('day3.txt') as f:
        data = [x.strip() for x in f.readlines()]
        print(parsemap(data, 3, 1))

def day3part2():
    with open('day3.txt') as f:
        data = [x.strip() for x in f.readlines()]
        print(parsemap(data, 1, 1) * \
              parsemap(data, 3, 1) * \
              parsemap(data, 5, 1) * \
              parsemap(data, 7, 1) * \
              parsemap(data, 1, 2))

if __name__=="__main__":
    day3test()
    day3part1()
    day3part2()
