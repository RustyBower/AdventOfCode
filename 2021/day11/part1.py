import numpy as np

with open('input') as f:
    data = f.read().splitlines()

data = [[int(x) for x in y] for y in data]

print(f"Before any steps:")
print(np.matrix(data))
print()

flashes = 0
for step in range(1000):
    points = [(x,y) for x in range(len(data)) for y in range(len(data))]
    for x, y in points:
        #print(x, y)
        #print(points)
        data[x][y] += 1
        # If value == 10, increase all surrounding
        if data[x][y] == 10:
            # Left
            if x > 0:
                points.append((x-1,y))
            # Right
            if x < len(data) - 1:
                points.append((x+1,y))
            # Up
            if y > 0:
                points.append((x,y-1))
            # Down
            if y < len(data) - 1:
                points.append((x,y+1))
            # Up Left
            if y > 0 and x > 0:
                points.append((x-1,y-1))
            # Up Right
            if y > 0 and x < len(data) -1:
                points.append((x+1,y-1))
            # Down Left
            if y < len(data) -1 and x > 0:
                points.append((x-1,y+1))
            # Down Right
            if y < len(data) - 1 and x < len(data) - 1:
                points.append((x+1,y+1))
        #print(np.matrix(data))

    # Reset all elements to 0 if > 9
    for x, y in [(x,y) for x in range(len(data)) for y in range(len(data))]:
        if data[x][y] >= 10:
            data[x][y] = 0
            flashes += 1

    print(f"After step {step+1}:")
    print(np.matrix(data))
    print(sum([sum(row) for row in data]))
    print()

print(flashes)
