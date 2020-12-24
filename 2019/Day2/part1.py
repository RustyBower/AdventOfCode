#!/usr/bin/env python


def opcode(data):
    data = [int(x) for x in data.split(',')]
    i = 0
    for v in data:
        if data[i] == 1:
            data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
            i += 4  # Reset Index
        if data[i] == 2:
            data[data[i+3]] = data[data[i+1]] * data[data[i+2]]
            i += 4  # Reset Index
        if data[i] == 99:
            break
    return ','.join(map(str,data))


if __name__ == '__main__':
    with open('day2.txt', 'r') as f:
        data = f.read()
        data = data.strip()
        print(opcode(data))
