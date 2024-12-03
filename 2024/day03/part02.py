import re

# pattern = r"mul\((\d+),(\d+)\)"
pattern = r"mul\((\d+),(\d+)\)|don\'t\(\)|do\(\)"

total = 0
enabled = True

with open("input.txt") as f:
    for line in f.readlines():
        # print(line)
        match = re.finditer(pattern, line)
        for x in match:
            print(x)
            if x.group().startswith("mul"):
                # print(x.groups()[0])
                print(int(x.groups()[0]), int(x.groups()[1]), int(x.groups()[0]) * int(x.groups()[1]))
                if enabled:
                    total += int(x.groups()[0]) * int(x.groups()[1])
            else:
                if x.group() == "don't()":
                    enabled = False
                else:
                    enabled = True
            # total += int(x[0]) * int(x[1])

print(total)
