safe = 0

with open("day02.txt") as f:
    for line in f.readlines():
        # print(line)
        line = list(map(int, line.split()))

        # Validate the line is ascending or descending
        if line != sorted(line, reverse=False) and line != sorted(line, reverse=True):
            continue

        # print(line, len(line))
        for x in range(len(line) - 1):
            # print(line[x], line[x + 1])
            if abs(line[x] - line[x + 1]) > 3:
                # print("Error: too far apart", line[x], line[x + 1], abs(line[x] - line[x + 1]))
                break
            if abs(line[x] == line[x + 1]):
                # print("Error: cannot be the same number")
                break
        else:
            safe += 1

print(safe)
