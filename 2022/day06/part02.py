#!/usr/bin/env python

#with open('day06.txt') as f:
with open('day06.txt') as f:
    data = f.read().splitlines()

for row in data:
    print(row)
    for x in range(0, len(row) - 13):
        #print(x, row[x:x+4])
        # Skip if there aren't 4 unique characters
        if len(set(row[x:x+14])) < 14:
            continue
        else:
            print(x, row[x:x+14], x+14)
            break
    print('-' * 10)