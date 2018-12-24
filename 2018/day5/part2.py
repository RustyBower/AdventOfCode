from string import ascii_lowercase

with open('day5.txt') as f:
  line = f.readlines()[0].strip()

  # Remove unit
  for letter in ascii_lowercase:
    data = line
    data = data.replace(letter, '')
    data = data.replace(letter.upper(), '')

    go = True
    while go:
      # Loop over the string
      for i, c in enumerate(data):
        # Check if lowercase
        if c.islower():
          # Check if next letter is uppercase version of that letter
          try:
            if c.upper() == data[i+1]:
              data = data.replace(c + data[i+1], '')
              break
          # Handle the index error because we're lazy
          except IndexError:
            go = False
            break
        # Otherwise uppercase
        else:
          # Check if next letter is lowercase version of that letter
          try:
            if c.lower() == data[i+1]:
              data = data.replace(c + data[i+1], '')
              break
          # Handle the index error because we're lazy
          except IndexError:
            go = False
            break

    print(letter, len(data))
