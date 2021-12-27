#!/usr/bin/env python
from itertools import product

with open("input") as f:
    data = f.read().splitlines()

data = data[0].split()

x_range = data[2][2:-1]
y_range = data[3][2:]

x_min, x_max = map(int, x_range.split(".."))
y_min, y_max = map(int, y_range.split(".."))

valid_coords = []

for x_init, y_init in list(product(range(100), list(range(-100, 100)))):
    delta_x, delta_y = x_init, y_init
    x, y = 0, 0
    # x_sum = sum([x for x in range(x_init, 0, -1)])
    # print(x_sum)
    # if x_sum < x_min or x_sum > x_max:
    #     print("Invalid Initial X")
    #     continue
    while True:
        # print(x, y)
        # Break on invalid X
        x_sum = sum([x for x in range(x_init, 0, -1)])
        if x_sum < x_min and x_sum > x_max:
            break

        if (
            x >= x_min
            and x <= x_max
            and y <= max(y_min, y_max)
            and y >= min(y_min, y_max)
        ):
            valid_coords.append((x_init, y_init))
            break

        # Break if we're too low
        if y <= min(y_min, y_max):
            break

        # Increment data
        x += delta_x
        y += delta_y
        if delta_x > 0:
            delta_x -= 1
        delta_y -= 1
    # print()
print(valid_coords)

max_velocity = sum([x for x in range(max(valid_coords, key=lambda k: k[1])[1], 0, -1)])
print(max(valid_coords, key=lambda k: k[1]), max_velocity)


# valid_x = []
# # Check for valid initial x and y coordinates
# for x_init in range(10):
#     x_sum = sum([x for x in range(x_init, 0, -1)])
#     # Check for valid y coordinates based on valid x
#     if x_sum >= x_min and x_sum <= x_max:
#         valid_x.append(x_init)
# # print(valid_x)

# valid_y = []
# for init_y in range(10, -10, -1):
#     y = 0
#     delta_y = init_y
#     while True:
#         y += delta_y
#         print(y)
#         if y >= min(y_min, y_max) and y <= max(y_min, y_max):
#             valid_y.append(init_y)
#             break
#         # Break if we're too low
#         if y <= min(y_min, y_max):
#             break
#         delta_y -= 1
# print(valid_y)
