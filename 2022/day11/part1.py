#!/usr/bin/env python
import functools
import heapq
import operator

class monkey:
    def __init__(self, number, items, operation, test, test_true, test_false):
        self.number = number
        self.items = items
        self.operation = operation
        self.test = test
        self.test_true = test_true
        self.test_false = test_false
        self.inspected_count = 0

    def calculate_worry(self, item, operation):
        operator = operation.split()[1]
        if operation.split()[2] == 'old':
            num = item
        else:
            num = int(operation.split()[2])

        if operator == '+':
            #print('    Worry level increases by', item, 'to', item + num)
            return item + num
        elif operator == '*':
            #print('    Worry level is multiplied by', item, 'to', item * num)
            return item * num
    def test_item(self, item):
        self.items = self.items[1:]
        #print(item, self.test, item % self.test)
        if (item % self.test) != 0:
            #print('    Current worry level is not divisible by', self.test)
            return item, self.test_false
        else:
            #print('    Current worry level is divisible by', self.test)
            return item, self.test_true


with open('input.txt') as f:
    data = f.read().splitlines()

monkeys = []
for i, x in enumerate(range(0, len(data), 7)):
    #print(i, x)
    #print(data[x:x+6])
    items = list(map(int, data[x+1].split(': ')[1].split(', ')))
    operation = data[x+2].split('=')[-1].strip()
    test = int(data[x+3].strip().split()[-1])
    test_true = int(data[x+4].strip().split()[-1])
    test_false = int(data[x+5].strip().split()[-1])
    m = monkey(i, items, operation, test, test_true, test_false)
    #print(m.__dict__)
    monkeys.append(m)
    #print()

modulo = functools.reduce(operator.mul, [m.test for m in monkeys])

for x in range(0, 10000):
    if x + 1 in [1, 20, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]:
        print(f'== After round {x+1} ==')
    #print('==', 'Round', x + 1, '==')
    for m in monkeys:
        #print('Monkey', m.number)
        for i, v in enumerate(m.items):
            #print(i, v)
            #print('  Monkey inspects an item with a worry level of', v)
            m.inspected_count += 1
            m.items[0] = m.calculate_worry(v, m.operation)
            #print('    Monkey gets bored with item. Worry level is divided by 3 to', m.items[0] // 3)
            m.items[0] = m.items[0] % modulo
            item, next_monkey = m.test_item(m.items[0])
            #print('    Item with worry level', item, 'is thrown to monkey', next_monkey)
            monkeys[next_monkey].items.append(item)
        if x + 1 in [1, 20, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]:
            print(f'Monkey {m.number} inspected items {m.inspected_count} times.')
    '''
    print()
    print(f'After round {x+1}, the monkeys are holding items with these worry levels:')
    for m in monkeys:
        print(f'Monkey {m.number}:', ', '.join(map(str, m.items)))
    print()
    '''

'''
for m in monkeys:
    print(f'Monkey {m.number} inspected items {m.inspected_count} times.')
'''

print([m.inspected_count for m in monkeys])
print(functools.reduce(operator.mul, heapq.nlargest(2, [m.inspected_count for m in monkeys])))
