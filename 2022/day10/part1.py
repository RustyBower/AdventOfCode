#!/usr/bin/env python

with open('input.txt') as f:
    data = f.read().splitlines()

x = 1
cycle = 1
signal_strength = 0

def check_signal(cycle, register):
    #print(cycle, register)
    if (cycle - 20) % 40 == 0:
        print(cycle, register, cycle * register)
        return cycle * register
    return 0

for inst in data:
    match inst.split():
        case['noop']:
            signal_strength += check_signal(cycle, x)
            cycle += 1
        case['addx', value]:
            # Increment cycle by 1
            for _ in range(0, 2):
                signal_strength += check_signal(cycle, x)
                cycle += 1
            x += int(value)
        case _:
            print('base case')

print(signal_strength)
