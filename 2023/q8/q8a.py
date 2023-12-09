import re

def main():
  f = open("./q8_input.txt", "r")

  directions = list(f.readline().strip())
  f.readline()

  elements = {}
  for line in f:
    data = line.strip().split('=')
    direction_elements = re.findall("\w+", data[1])
    elements[data[0].strip()] = (direction_elements[0], direction_elements[1])

  steps = 0
  current_cell = 'AAA'
  while current_cell != 'ZZZ':
    direction = 0 if directions[steps % len(directions)] == 'L' else 1
    current_cell = elements[current_cell][direction]
    steps += 1
  print(steps)
  

main()