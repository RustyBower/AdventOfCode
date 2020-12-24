#!/usr/bin/env python
import copy

acc = 0
lines = []

def execute(instructions, line):
    global acc
    global lines
    if line in lines:
        return False
    lines.append(line)
    if line >= len(instructions):
        return acc
    #print(instructions[line], acc)
    operation = instructions[line].split()[0]
    argument = int(instructions[line].split()[1])
    if operation == 'nop':
        line += 1
        if execute(instructions, line):
            return acc
    elif operation == 'acc':
        line += 1
        acc += argument
        if execute(instructions, line):
            return acc
    elif operation == 'jmp':
        line += argument
        if execute(instructions, line):
            return acc
    else:
        print('ELSE', operation)


def day8test():
    with open('test.txt') as f:
        data = f.readlines()
        data = [x.strip() for x in data]
        execute(data, 0)
        print(acc)

def day8part1():
    with open('day8.txt') as f:
        data = f.readlines()
        data = [x.strip() for x in data]
        execute(data, 0)
        print(acc)

def day8part2():
    with open('day8.txt') as f:
        data = f.readlines()
        data = [x.strip() for x in data]
        jmps = [i for i, x in enumerate(data) if 'jmp' in x]
        for x in jmps:
            copied = copy.deepcopy(data)
            global acc, lines
            acc = 0
            lines = []
            copied[x] = copied[x].replace('jmp', 'nop')
            #print(data)
            #print(copied)
            #print(execute(copied, 0))
            if execute(copied, 0):
                #print("LINE:", x + 1)
                print(acc)
            #print('-' * 10)
        #print(acc)

if __name__=="__main__":
    #day8test()
    day8part1()
    #day8part2()
