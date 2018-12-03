# Populate array
# Do array copy because Python tries to help and points all the None'd arrays at the same pointer
fabric = []
columns = [None] * 1000
rows = 0
while rows < 1000:
  fabric.append(columns.copy())
  rows += 1

with open('day3.txt') as f:
  for line in f:
    # Parse all our inputs
    number = int(line.strip().split()[0].strip('#'))
    x = int(line.strip().split()[2].split(',')[0])
    y = int(line.strip().split()[2].split(',')[1].strip(':'))
    width = int(line.strip().split()[3].split('x')[0])
    height = int(line.strip().split()[3].split('x')[1])

    # Populate Array
    i = 0
    while i < height:
      j = 0
      while j < width:
        if fabric[y+i][x+j] is None:
          fabric[y+i][x+j] = number
        else:
          fabric[y+i][x+j] = 'X'
        j += 1
      i += 1

# Find number of occurances of overlap
print(sum(z.count('X') for z in fabric))
