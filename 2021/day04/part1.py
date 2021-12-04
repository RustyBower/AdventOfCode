#!/usr/bin/env python

def check_board(board, numbers):
    #print(numbers)
    #print(board)
    for row in board:
        row = [int(x) for x in row.split()]
        #print(row)
        if all((x in numbers for x in row)):
            print(board, numbers)
            unmarked = list(set([int(x) for x in ' '.join(board).split()]) - set(numbers))
            print(unmarked, numbers[-1])
            return unmarked, numbers[-1]

    for i in range(5):
        column = [int(x.split()[i]) for x in board]
        if all((x in numbers for x in column)):
            print(board, numbers)
            unmarked = list(set([int(x) for x in ' '.join(board).split()]) - set(numbers))
            print(unmarked, numbers[-1])
            return unmarked, numbers[-1]

    return False, False

with open('day4.txt') as f:
    data = f.read().splitlines()

#print(data)
numbers = data[0].split(',')
boards = []
for i in range(1, len(data), 6):
    board = data[i+1:i+6]
    boards.append(board)

class Found(Exception): pass
try:
    for i, x in enumerate(numbers):
        for board in boards:
            unmarked, number = check_board(board, [int(x) for x in numbers[0:i+1]])
            #print(unmarked, number)
            if unmarked:
                raise Found

except Found:
    print(sum(unmarked) * number)
