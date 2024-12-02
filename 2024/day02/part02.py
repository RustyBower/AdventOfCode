from itertools import combinations

safe = 0


def check_sorted(line):
    return line == sorted(line, reverse=False) or line == sorted(line, reverse=True)


def check_levels(line):
    for x in range(len(line) - 1):
        # print(line[x], line[x + 1])
        if abs(line[x] - line[x + 1]) > 3:
            # print("Error: too far apart", line[x], line[x + 1], abs(line[x] - line[x + 1]))
            return False
        if abs(line[x] == line[x + 1]):
            # print("Error: cannot be the same number")
            return False
    else:
        return True


with open("day02.txt") as f:
    for line in f.readlines():
        # print(line)
        line = list(map(int, line.split()))
        # print(line)

        # Validate the line is ascending or descending
        if check_sorted(line) and check_levels(line):
            # print("safe default")
            safe += 1
            continue

        for line in list(combinations(line, len(line) - 1)):
            # print(line)
            if check_sorted(list(line)) and check_levels(list(line)):
                # print(line, "safe")
                safe += 1
                break

print(safe)
