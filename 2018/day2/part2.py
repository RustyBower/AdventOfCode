# I don't like this, but it's quick and dirty
string_list = []

with open('day2.txt') as f:
  for line in f:
    string_list.append(line.strip())

for index, first_string in enumerate(string_list):
  for second_string in string_list[index+1:]:
    diff_count = 0
    for a, b in zip(first_string, second_string):
      if a != b:
        diff_count += 1
    if diff_count == 1:
      common_letters = ""
      for a, b in zip(first_string, second_string):
        if a == b:
          common_letters += a
      print(common_letters)

