#!/usr/bin/env python
from pprint import pprint

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path or node.isupper():
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
pprint(all_paths)
print(len(all_paths))
