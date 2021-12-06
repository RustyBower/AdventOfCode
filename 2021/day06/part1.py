#!/usr/bin/env python

with open('day6.txt') as f:
    data = f.read().strip().split(',')

days = 80

data = [int(x) for x in data]
print('Initial state:', ','.join(map(str, data)))

for d in range(1, days + 1):
    data[:] = [d - 1 for d in data]

    for i, x in enumerate(data):
        if x < 0:
            data[i] = 6
            data.append(8)

    if d == 1:
        print("After {:2} day: ".format(d), ','.join(map(str, data)))
    else:
        print("After {:2} days: {:<30}".format(d, ','.join(map(str, data))))

print(len(data))
