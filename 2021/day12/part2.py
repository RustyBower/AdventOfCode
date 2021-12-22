#!/usr/bin/env python
from collections import Counter
from pprint import pprint

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node == 'start':
            continue
        if len([x for x in Counter([x for x in path if x.islower() if x != 'start' if x != 'end']).values() if x > 1]) > 1:
            continue
        if path.count(node) <= 1 or node.isupper():
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

with open('input') as f:
    data = f.read().splitlines()

graph = {}
for edge in data:
    edge = edge.split('-')
    if edge[0] in graph.keys():
        graph[edge[0]].append(edge[1])
    else:
        graph[edge[0]] = [edge[1]]
    if edge[1] in graph.keys():
        graph[edge[1]].append(edge[0])
    else:
        graph[edge[1]] = [edge[0]]

pprint(graph)
print()
all_paths = find_all_paths(graph, 'start', 'end')
print(len(all_paths))
final_paths = []
for path in all_paths:
    counter = Counter(path)
    if counter['start'] > 1:
        continue
    elif len([x for x in Counter([x for x in path if x.islower() if x != 'start' if x != 'end']).values() if x > 1]) > 1:
        continue
    else:
        final_paths.append(path)
#pprint(all_paths)
pprint(final_paths)
print(len(final_paths))
