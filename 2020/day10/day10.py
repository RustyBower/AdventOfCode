#!/usr/bin/env python
import copy
import functools
import itertools
from anytree import AnyNode, Node, RenderTree

count = 0

@functools.lru_cache
def joltage(adapter_list, input_joltage, adapter_chain=[0], one_jolt_count=0, three_jolt_count=1):
    #print(adapter_list, input_joltage, adapter_chain)
    if not adapter_list:
        print(adapter_chain, one_jolt_count * three_jolt_count)
        return
    if input_joltage > max(adapter_list):
        print("MAX_JOLTAGE")
        return
    #print(adapter_list, input_joltage, adapter_chain)
    eligible_adapters = [x for x in adapter_list if x <= input_joltage + 3]
    eligible_adapters = min(eligible_adapters)
    #print(eligible_adapters)
    #print(eligible_adapters[0])
    if eligible_adapters - input_joltage == 1:
        one_jolt_count += 1
    if eligible_adapters - input_joltage == 3:
        three_jolt_count += 1
    input_joltage = eligible_adapters
    adapter_chain.append(eligible_adapters)
    adapter_list.remove(eligible_adapters)
    #print('-' * 10)
    joltage(adapter_list, input_joltage, adapter_chain, one_jolt_count, three_jolt_count)


@functools.lru_cache(maxsize=10)
def joltage2(adapter_list, input_joltage=0, adapter_chain=[0]):
    #print(adapter_list, input_joltage, adapter_chain)
    if not adapter_list:
        #print(adapter_chain)
        global count
        count += 1
        return
    eligible_adapters = [x for x in adapter_list if x <= input_joltage + 3]
    #print(eligible_adapters)
    adapter_chain2 = copy.deepcopy(adapter_chain)
    adapter_list2 = copy.deepcopy(adapter_list)
    for adapter in eligible_adapters:
        adapter_chain2.append(adapter)
        adapter_list2.remove(adapter)
        input_joltage = adapter
        if joltage2(adapter_list2, input_joltage, adapter_chain2):
            return


def day10test():
    with open('day10.txt') as f:
        data = f.readlines()
        data = [int(x.strip()) for x in data]
        max_joltage = max(data) + 3
        #print(data)
        #print(max_joltage)
        joltage(data, 0)


def day10part2():
    with open('test.txt') as f:
        data = f.readlines()
        data = [int(x.strip()) for x in data]
        data.append(0)
        data.append(max(data) + 3)
        data.sort()
        root = Node(0)
        print(data)
        for adapter in data:
            print(RenderTree(root))
            for child in [x for x in data if x <= adapter + 3 if x > adapter]:
                print(adapter, child)
            #tree[adapter] = [x for x in data if x <= adapter + 3 if x > adapter]
        print(root)
        print(RenderTree(root))

tree = {}

@functools.lru_cache
def recurseplz(index):
    if not tree[index]:
        return 1
    else:
        return(sum([recurseplz(x) for x in tree[index]]))


def ohgod():
    with open('day10.txt') as f:
        data = f.readlines()
        data = [int(x.strip()) for x in data]
        data.append(0)
        data.append(max(data) + 3)
        data.sort()
        #print(data)
        global tree
        for adapter in data:
            tree[adapter] = [x for x in data if x <= adapter + 3 if x > adapter]
        '''
        data.sort(reverse=True)
        newdict = {}
        newdict[data[0]] = 1
        for x in data[1:]:
            newdict[x] = sum(newdict[y] for y in tree[x])
        print(newdict)
        '''
        print(recurseplz(0))
        #print(tree)

if __name__=="__main__":
    #day10test()
    #day10part2()
    ohgod()
