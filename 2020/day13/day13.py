#!/usr/bin/env python
import operator

def part1():
    with open('day13.txt') as f:
        data = [x.strip() for x in f.readlines()]
        schedule = [(bus, bus - int(data[0]) % bus) for bus in [int(x) for x in data[1].split(',') if x.isdigit()]]
        #print(min(schedule, key=operator.itemgetter(1)))
        x = min(schedule, key=operator.itemgetter(1))
        print(x[0] * x[1])

def part2():
    with open('day13.txt') as f:
        data = [x.strip() for x in f.readlines()]
        data = data[1].split(',')
        c = 0
        while True:
        #for c in range(1068774, 1068797, 7):
            c += int(data[0])
            #print(c)
            for k, v in enumerate(data):
                #print(k, v)
                if v == 'x':
                    continue
                #print(k + c, v, (k + c) % int(v))
                if ((k + c) % int(v)) == 0:
                    continue
                else:
                    break
            else:
                return c

if __name__=="__main__":
    #part1()
    print(part2())
