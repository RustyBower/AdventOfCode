#!/usr/bin/env python
from collections import Counter, deque

with open('input') as f:
    data = f.read().splitlines()

counter = Counter()

for row in data:
    d = deque()
    for character in row:
        if character in ['(', '[', '{', '<']:
            d.append(character)
        else:
            c = d.pop()
            #print(c, character)
            '''
            if c == '(' and character == ')':
                print('good')
            elif c == '[' and character == ']':
                print('good')
            elif c == '{' and character == '}':
                print('good')
            elif c == '<' and character == '>':
                print('good')
            else:
                print('Shit is fucked')
                break
            '''
            if (c == '(' and character == ')') or \
                (c == '[' and character == ']') or \
                (c == '{' and character == '}') or \
                (c == '<' and character == '>'):
                pass
            else:
                print('Syntax Error:', row)
                counter[character] += 1
                break

print(counter[')'] * 3 + counter[']'] * 57 + counter['}'] * 1197 + counter['>'] * 25137)
