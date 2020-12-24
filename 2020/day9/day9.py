#!/usr/bin/env python
import operator
from collections import deque
from itertools import accumulate, combinations

def day9test():
    preamble = deque([None] * 5, maxlen=5)
    with open('test.txt') as f:
        for line in f:
            line = int(line.strip())
            #print(list(preamble))
            if None in preamble:
                preamble.append(line)
                continue
            if not [x for x in combinations(list(preamble), 2) if sum(x) == line]:
                print(line)
            preamble.append(line)
            #print('-' * 10)

def day9part1():
    preamble = deque([None] * 25, maxlen=25)
    with open('day9.txt') as f:
        for line in f:
            line = int(line.strip())
            #print(list(preamble))
            if None in preamble:
                preamble.append(line)
                continue
            if not [x for x in combinations(list(preamble), 2) if sum(x) == line]:
                print(line)
            preamble.append(line)
            #print('-' * 10)

def day9part2():
    number = 1038347917
    with open('day9.txt') as f:
        data = f.readlines()
        data = [int(x.strip()) for x in data]
        for x in range(len(data)):
            if [y for y in list(accumulate(data[x:], operator.add)) if y == number if data[x] != number]:
                #print(data[x:])
                offset = list(accumulate(data[x:], operator.add)).index(number) + 1
                contrange = data[x:x+offset]
                print(min(contrange) + max(contrange))

if __name__=="__main__":
    day9test()
    day9part1()
    day9part2()
