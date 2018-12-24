with open('day4-sorted.txt') as f:
  guardID = None
  guards = {}
  asleep, awake = None, None
  for line in f:
    line = line.strip()
    if "begins shift" in line:
      asleep, awake = None, None
      guardID = line.split()[3].strip('#')
      if guardID not in guards.keys():
        for x in range(60):
          guards[guardID] = {}
    if "falls asleep" in line and guardID:
      asleep = line.split()[1].split(':')[1].strip(']')
    if "wakes up" in line and guardID:
      awake = line.split()[1].split(':')[1].strip(']')
      if int(asleep) < int(awake):
        for x in range(int(asleep), int(awake)):
          if x in guards[guardID]:
            guards[guardID][x] += 1
          else:
            guards[guardID][x] = 1
      else:
        for x in range(int(asleep), int(awake) + 60):
          if x in guards[guardID]:
            guards[guardID][x % 60] += 1
          else:
            guards[guardID][x % 60] = 1
          

for key, value in sorted(guards.items(), key=lambda i: sorted(i[1].values()), reverse=True):
  print(key, sum(value.values()), value)
