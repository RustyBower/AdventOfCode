#!/usr/bin/env python
import copy
import math
from collections import Counter
from itertools import tee


def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return ["".join(pair) for pair in zip(a, b)]


with open("input") as f:
    data = f.read().splitlines()

template = data[0]
rules = [tuple(x.split(" -> ")) for x in data[2:]]

pairs = pairwise(template)
counter = Counter(pairs)
# print(f"Template:     {template}")

for x in range(1, 41):
    working = copy.deepcopy(counter)
    for rule in rules:
        if working[rule[0]] > 0:
            counter[rule[0][0] + rule[1]] += working[rule[0]]
            counter[rule[1] + rule[0][1]] += working[rule[0]]
            if counter[rule[0]] > 0:
                counter[rule[0]] -= working[rule[0]]
    # print(f"After step {x}: {sum(counter.values()) + 1}")

print(counter)
counts = Counter()
for key, value in counter.items():
    print(key, value)
    for k in key:
        counts[k] += value
        print(k, value, counts)

most_common = int(math.ceil(counts.most_common()[0][1] / 2))
least_common = int(math.ceil(counts.most_common()[-1][1] / 2))
print(most_common, least_common)
print(most_common - least_common)
