#!/usr/bin/env python
from collections import Counter
from itertools import tee

def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return [''.join(pair) for pair in zip(a, b)]

#with open('input') as f:
with open('test') as f:
    data = f.read().splitlines()

template = data[0]
rules = [tuple(x.split(' -> ')) for x in data[2:]]

print("Template:    ", template)
for x in range(40):
    print(f'{x} - {len(template)}')
    pairs = pairwise(template)
    '''
    for rule, value in rules:
        if rule in pairs:
            inserted = rule[0] + value + rule[1]
            pairs = [inserted if x == rule else x for x in pairs]
    '''
    for i, pair in enumerate(pairs):
        for rule, value in rules:
            if pair == rule:
                inserted = rule[0] + value + rule[1]
                pairs[i] = inserted
                continue
    template = ''.join([x[:-1] for x in pairs[:-1]] + [pairs[-1]])
    #print(f"After step {x+1}: {template}")
common = Counter(template).most_common()
most_common = common[0][1]
least_common = common[-1][1]
print(most_common - least_common)
