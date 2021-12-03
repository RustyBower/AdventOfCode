#!/usr/bin/env python

with open('day3.txt') as f:
    data = f.read().splitlines()

# print(data)

gamma = ''
epsilon = ''

for i in range(len(data[0])):
    bit = [int(x[i]) for x in data]
    gamma += str(max(set(bit), key = bit.count))
    epsilon += str(min(set(bit), key = bit.count))

# print(gamma, epsilon)
print(int(gamma, 2) * int(epsilon, 2))
