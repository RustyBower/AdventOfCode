#!/usr/bin/env
from itertools import combinations


def day1part1():
    with open('day1.txt') as f:
        data = f.readlines()

    data = [int(x.strip()) for x in data]

    answer = [x for x in combinations(data, 2) if x[0] + x[1] == 2020][0]
    print(answer[0] * answer[1])


def day1part2():
    with open('day1.txt') as f:
        data = f.readlines()

    data = [int(x.strip()) for x in data]

    answer = [x for x in combinations(data, 3) if x[0] + x[1] + x[2] == 2020][0]
    print(answer[0] * answer[1] * answer[2])

if __name__=="__main__":
    day1part1()
    day1part2()
