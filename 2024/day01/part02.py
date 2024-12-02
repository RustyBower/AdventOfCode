from collections import Counter

with open("day01.txt") as f:
    left, right = list(), Counter()
    for line in f.readlines():
        a, b = map(int, line.split())
        left.append(a)
        right[b] += 1

# print(left, right)

print(sum(x * right[x] for x in left))
