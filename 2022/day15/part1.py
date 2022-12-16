#!/usr/bin/env python
from collections import defaultdict

def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

def merge_ranges(ranges):
    """
    Merge overlapping and adjacent ranges and yield the merged ranges
    in order. The argument must be an iterable of pairs (start, stop).

    >>> list(merge_ranges([(5,7), (3,5), (-1,3)]))
    [(-1, 7)]
    >>> list(merge_ranges([(5,6), (3,4), (1,2)]))
    [(1, 2), (3, 4), (5, 6)]
    >>> list(merge_ranges([]))
    []
    """
    ranges = iter(sorted(ranges))
    current_start, current_stop = next(ranges)
    for start, stop in ranges:
        if start > current_stop:
            # Gap between segments: output current segment and start a new one.
            yield current_start, current_stop
            current_start, current_stop = start, stop
        else:
            # Segments adjacent or overlapping: merge.
            current_stop = max(current_stop, stop)
    yield current_start, current_stop


invalid = defaultdict(list)
sensors = set()
beacons = set()

for line in open(0):
    print(line.strip())
    line = line.split()
    sensor = int(line[2].split('=')[1].strip(',:')), int(line[3].split('=')[1].strip(',:'))
    beacon = int(line[8].split('=')[1].strip(',:')), int(line[9].split('=')[1].strip(',:'))
    dist = manhattan(sensor, beacon)
    sensors.add(sensor)
    beacons.add(beacon)
    #print(sensor)
    #print(beacon)
    #print(dist)

    for i, v in enumerate(range(sensor[1] - dist, sensor[1] + dist + 1), start=-dist):
        #print(i, v)
        invalid[v].append((sensor[0] - (dist - abs(i)), sensor[0] + (dist - abs(i))))
        #print()

print()
#print([abs(x[0]) + abs(x[1]) + 1 for x in merge_ranges(invalid[10])])
row = 2000000
ranges = list(merge_ranges(invalid[row]))
print(ranges)
for r in ranges:
    print('r', r)
    for s in sensors:
        if s[1] == row:
            print('s', s)
            if r[0] <= s[0] <= r[1]:
                print(r)
                ranges.remove(r)
                ranges.append((r[0], s[0] - 1))
                ranges.append((s[0] + 1, r[1]))
    for b in beacons:
        if b[1] == row:
            print('b', b)
            if r[0] <= b[0] <= r[1]:
                print(r)
                ranges.remove(r)
                ranges.append((r[0], b[0] - 1))
                ranges.append((b[0] + 1, r[1]))

print(ranges)
print(sum([len(range(x[0],x[1])) for x in ranges]) + len(ranges))
