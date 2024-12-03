import re

pattern = r"mul\((\d+),(\d+)\)"

total = 0

with open("input.txt") as f:
    for line in f.readlines():
        # print(line)
        match = re.findall(pattern, line)
        for x in match:
            print(int(x[0]), int(x[1]), int(x[0]) * int(x[1]))
            total += int(x[0]) * int(x[1])

print(total)
