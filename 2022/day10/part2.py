#!/usr/bin/env python

def draw_screen(screen, cycle, x):
    #print('Sprite position:', sprite_position(x))
    row = (cycle - 1) // 40
    pixel = cycle % 40
    #print(cycle, row, pixel)
    if pixel - 1 <= x + 1 and pixel - 1 >= x - 1:
        screen[row][pixel-1] = '#'
    else:
        screen[row][pixel-1] = '.'
    return screen

def print_screen(screen):
    print('\n'.join(''.join(row) for row in screen))

def sprite_position(x):
    sprite = ['.' for x in range(40)]
    sprite[x-1], sprite[x], sprite[x+1] = '#', '#', '#'
    return ''.join(sprite)

with open('input.txt') as f:
    data = f.read().splitlines()

x = 1
cycle = 1
screen = [['' for x in range(40)] for y in range(6)]
#print(screen)

print('Sprite position:', sprite_position(x))
print()

for inst in data:
    match inst.split():
        case['noop']:
            #screen[cycle-1] = '.'
            screen = draw_screen(screen, cycle, x)
            #print_screen(screen)
            cycle += 1
        case['addx', value]:
            # Increment cycle by 1
            for _ in range(0, 2):
                screen = draw_screen(screen, cycle, x)
                #print_screen(screen)
                cycle += 1
            x += int(value)
        case _:
            print('base case')

print('\n'.join(''.join(row) for row in screen))
