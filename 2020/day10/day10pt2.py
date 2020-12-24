#!/usr/bin/env python
import copy
import itertools

perms = {}


def jolt(adapter_list, input_joltage=0, adapter_chain=[]):
    print('-' * 10)
    print(adapter_list, input_joltage, adapter_chain)
    print([x for x in adapter_list if x <= input_joltage + 3 if x > input_joltage])
    for adapter in [x for x in adapter_list if x <= input_joltage + 3 if x > input_joltage]:
        adapter_chain.append(adapter)
        adapter_list.remove(adapter)
        return jolt(copy.deepcopy(adapter_list), adapter, copy.deepcopy(adapter_chain))
    print('-' * 10)
    return adapter_chain

'''
Check the index of the next thing (so 4 -> 5,6,7), if the target has a value of 1, then we can exit our recursion, otherwise we need to do recursion on that next value

4 -> [5,6,7]
5 -> [6,7]
6 return 1
7 returns 1
'''


'''
(0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 6, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 6, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 6, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 7, 10, 12, 15, 16, 19, (22)
'''
with open('test.txt') as f:
    data = f.readlines()
    data = [int(x.strip()) for x in data]
    data.append(0)
    data.append(max(data) + 3)
    data.sort()
    for adapter in data:
        perms[adapter] = len([x for x in data if x <= adapter + 3 if x > adapter])
    print(jolt(data))
