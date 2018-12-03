from collections import Counter
two_letters = 0
three_letters = 0

with open('day2.txt') as f:
  for line in f:
    # Hacky hack to add to our counter after iterating over all letters
    add_two, add_three = False, False

    # Use existing Python library to create dictionary of letter counts
    counter = Counter(line.strip())
    
    # Loop over our dictionary
    for letter in counter.keys():
      if(counter[letter] == 2):
        add_two = True
      if(counter[letter] == 3):
        add_three = True
    
    # Add to our ongoing counter
    if add_two:
      two_letters += 1
    if add_three:
      three_letters += 1

print(two_letters * three_letters)
