frequency = 0
frequency_list = set()
boats = True
while boats:
  with open('day1.txt') as f:
    for line in f:
      delta = int(line.strip())
      frequency += delta 
      if frequency in frequency_list:
        print("Duplicate Frequency Found:", frequency)
        boats = False
        break
      frequency_list.add(frequency)
