import re
import math

def main():
  f = open("./q12_test_input.txt", "r")

  choices = 0
  for line in f:
    line = line.strip()
    groups = re.findall("(?:#|\?)+", line)
    data = re.findall("\d+", line)
    
    # Try matching each piece of data to a group
    if len(groups) == len(data):
      print('yes')
      for i in range(len(groups)):
        a = math.comb(len(groups[i]), int(data[i]))

    i = 0
    for group in groups:
      current_group_size = 0
      possible_groups = []
      while current_group_size < len(group):
        possible_groups.append(i)
        current_group_size += int(data[i]) + 1 # Plus 1 to account for space
        choices += 1

  print(choices)

main()