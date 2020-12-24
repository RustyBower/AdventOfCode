#!/usr/bin/env python

def checkString(first, second, character, password):
    count = password.count(character)
    if count >= first and count <= second:
        return True
    else:
        return False


def day2test():
    # 2-9 c: ccccccccc
    count = 0
    with open('test.txt') as f:
        for line in f:
            line = line.strip()
            print(line)
            firstchar = int(line.split()[0][0])
            secondchar = int(line.split()[0].split('-')[1])
            character = line.split()[1][0]
            password = line.split()[2]
            if checkString(firstchar, secondchar, character, password):
                count += 1
    return count


def day2part1():
    # 2-9 c: ccccccccc
    count = 0
    with open('day2.txt') as f:
        for line in f:
            line = line.strip()
            print(line)
            firstchar = int(line.split()[0].split('-')[0])
            secondchar = int(line.split()[0].split('-')[1])
            character = line.split()[1][0]
            password = line.split()[2]
            if checkString(firstchar, secondchar, character, password):
                count += 1
    return count


def day2part2():
    # 2-9 c: ccccccccc
    count = 0
    with open('day2.txt') as f:
        for line in f:
            line = line.strip()
            print(line)
            firstchar = int(line.split()[0].split('-')[0]) - 1
            secondchar = int(line.split()[0].split('-')[1]) - 1
            character = line.split()[1][0]
            password = line.split()[2]
            print(firstchar, secondchar, password, password[firstchar], password[secondchar])
            if (password[firstchar] == character) ^ (password[secondchar] == character):
                count += 1
    return count


if __name__=="__main__":
    print(day2test())
    print(day2part1())
    print(day2part2())
