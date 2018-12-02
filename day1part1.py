count = 0
with open('day1.txt') as f:
  for line in f:
    frequency = float(line.strip())
    count += frequency
print(count)
