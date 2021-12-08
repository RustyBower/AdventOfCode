#!/usr/bin/env python

with open('input.txt') as f:
    data = f.read().splitlines()

total = 0
for row in data:
    mapping = {}
    patterns = row.split(' | ')[0]
    output = row.split(' | ')[1]
    #print('patterns:', patterns)
    #print('output:', output)

    one   = [x for x in patterns.split(' ') if len(x) == 2][0]  # 1
    four  = [x for x in patterns.split(' ') if len(x) == 4][0]  # 4
    seven = [x for x in patterns.split(' ') if len(x) == 3][0]  # 7
    eight = [x for x in patterns.split(' ') if len(x) == 7][0]  # 8
    six   = [x for x in patterns.split(' ') if len(x) == 6 if not set(one).issubset(set(x))][0]
    nine  = [x for x in patterns.split(' ') if len(x) == 6 if set(four).issubset(set(x))][0]
    zero  = [x for x in patterns.split(' ') if len(x) == 6 if not set(nine).issubset(set(x)) if not set(six).issubset(set(x))][0]
    three = [x for x in patterns.split(' ') if len(x) == 5 if set(one).issubset(set(x))][0]
    five  = [x for x in patterns.split(' ') if len(x) == 5 if set(x).issubset(set(nine)) if set(x) != set(three)][0]
    two   = [x for x in patterns.split(' ') if len(x) == 5 if not set(x).issubset(set(nine)) if set(x) != set(three)][0]

    mapping[''.join(sorted(one))] = 1
    mapping[''.join(sorted(four))] = 4
    mapping[''.join(sorted(seven))] = 7
    mapping[''.join(sorted(eight))] = 8
    mapping[''.join(sorted(six))] = 6
    mapping[''.join(sorted(nine))] = 9
    mapping[''.join(sorted(zero))] = 0
    mapping[''.join(sorted(three))] = 3
    mapping[''.join(sorted(five))] = 5
    mapping[''.join(sorted(two))] = 2
    #print(mapping)

    value = int(''.join(map(str, [mapping[''.join(sorted(x))] for x in output.split(' ')])))
    #print(value)
    total += value

print(total)
