with open("day01.txt") as f:
    left, right = list(), list()
    for line in f.readlines():
        a, b = map(int, line.split())
        left.append(a)
        right.append(b)

left = sorted(left)
right = sorted(right)

# print(left, right)

print(sum(abs(x[0] - x[1]) for x in zip(left, right)))
