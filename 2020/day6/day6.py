#!/usr/bin/env python
from operator import and_
from functools import reduce

def day6test():
    with open('day6.txt') as f:
        count = 0
        data = f.read()
        data = [x.split('\n') for x in data.split('\n\n')]
        print(data)
        for group in data:
            print(group)
            count += len(set(list(''.join(group))))
        print(count)

def day6part2():
    with open('day6.txt') as f:
        count = 0
        data = f.read()
        data = [x.split('\n') for x in data.split('\n\n')]
        print(data)
        print('-' * 10)
        for group in data:
            print(group)
            count += len(reduce(and_, [set(x) for x in group if x]))
        return count

if __name__=="__main__":
    print(day6part2())
