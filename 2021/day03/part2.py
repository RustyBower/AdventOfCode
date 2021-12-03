#!/usr/bin/env python

with open('day3.txt') as f:
#with open('test.txt') as f:
    data = f.read().splitlines()

oxygen = data.copy()
co2 = data.copy()

for i in range(len(data[0])):
    oxygen_bits = [int(x[i]) for x in oxygen]
    co2_bits = [int(x[i]) for x in co2]

    #print(data, oxygen_bits, oxygen_bits.count(0), oxygen_bits.count(1))
    if len(oxygen) > 1:
        if oxygen_bits.count(1) > oxygen_bits.count(0):
            oxygen = [x for x in oxygen if int(x[i]) == 1]
        elif oxygen_bits.count(0) > oxygen_bits.count(1):
            oxygen = [x for x in oxygen if int(x[i]) == 0]
        else:
            oxygen = [x for x in oxygen if int(x[i]) == 1]

    #print(data, co2_bits, co2_bits.count(0), co2_bits.count(1))
    if len(co2) > 1:
        if co2_bits.count(1) > co2_bits.count(0):
            co2 = [x for x in co2 if int(x[i]) == 0]
        elif co2_bits.count(0) > co2_bits.count(1):
            co2 = [x for x in co2 if int(x[i]) == 1]
        else:
            co2 = [x for x in co2 if int(x[i]) == 0]

print(int(oxygen[0], 2) * int(co2[0], 2))
