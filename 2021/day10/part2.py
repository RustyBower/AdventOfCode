#!/usr/bin/env python
from collections import Counter, deque

with open('input') as f:
    data = f.read().splitlines()

incomplete = data.copy()
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
                #print('Syntax Error:', row)
                incomplete.remove(row)
                break
    
data = incomplete 
#data = ['<{([{{}}[<[[[<>{}]]]>[]]']

scores = []
for row in data:
    score = 0
    d = deque()
    for character in row:
        if character in ['(', '[', '{', '<']:
            d.append(character)
        else:
            c = d.pop()
            if (c == '(' and character == ')') or \
                (c == '[' and character == ']') or \
                (c == '{' and character == '}') or \
                (c == '<' and character == '>'):
                pass

    d.reverse()
    for c in d:
        score = score * 5
        if c == '(':
            score += 1
        elif c == '[':
            score += 2
        elif c == '{':
            score += 3
        elif c == '<':
            score += 4
        else:
            print('Invalid Character')
    scores.append(score)
scores = sorted(scores)
print(scores[int(len(scores)/2)])
