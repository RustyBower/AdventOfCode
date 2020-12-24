#!/usr/bin/env python
class Bags:
    def __init__(self, color, children=[]):
        self.color = color
        self.children = children

    #def __str__(self):
        #print(self.color)


def bagsearch(bags, color):
    #if not bags[color].children:
        #return False
    #print(bags[color].children)
    if 'shiny gold' in bags[color].children:
        return True
    else:
        for child in bags[color].children:
            if bagsearch(bags, child):
                return True



def day7test():
    with open('test.txt') as f:
        bags = {}
        for line in f:
            line = line.strip().strip('.')
            color = line.split(' bags contain ')[0]
            children = line.split(' bags contain ')[1].split(', ')
            c = []
            if children[0] != 'no other bags':
                for child in children:
                    #c.extend(int(child.split(' ', 1)[0]) * [child.split(' ', 1)[1].rstrip(' bags')])
                    c.extend([child.split(' ', 1)[1].rstrip(' bags')])
            bags[color] = Bags(color=color, children=c)
        count = 0
        for k, v in bags.items():
            if bagsearch(bags, k):
                count += 1
                continue
        print(count)


def day7part1():
    with open('day7.txt') as f:
        bags = {}
        for line in f:
            line = line.strip().strip('.')
            color = line.split(' bags contain ')[0]
            children = line.split(' bags contain ')[1].split(', ')
            c = []
            if children[0] != 'no other bags':
                for child in children:
                    #c.extend(int(child.split(' ', 1)[0]) * [child.split(' ', 1)[1].rstrip(' bags')])
                    c.extend([child.split(' ', 1)[1].rsplit(' ', 1)[0]])
            bags[color] = Bags(color=color, children=c)
        count = 0
        for k, v in bags.items():
            if bagsearch(bags, k):
                count += 1
                continue
        print(count)


count = 0

def count_bags(bags, color):
    global count
    count += len(bags.get(color).children)
    for child in bags.get(color).children:
        count_bags(bags, child)


def day7part2():
    with open('day7.txt') as f:
        bags = {}
        for line in f:
            line = line.strip().strip('.')
            color = line.split(' bags contain ')[0]
            children = line.split(' bags contain ')[1].split(', ')
            c = []
            if children[0] != 'no other bags':
                for child in children:
                    #c.extend(int(child.split(' ', 1)[0]) * [child.split(' ', 1)[1].rstrip(' bags')])
                    #c.extend([child.split(' ', 1)[1].rsplit(' ', 1)[0]])
                    c.extend(int(child.split(' ', 1)[0]) * [child.split(' ', 1)[1].rsplit(' ', 1)[0]])
            bags[color] = Bags(color=color, children=c)
        #print(count_bags(bags, 'shiny gold'))
        count_bags(bags, 'shiny gold')
        print(count)

if __name__=="__main__":
    day7test()
    day7part1()
    day7part2()
