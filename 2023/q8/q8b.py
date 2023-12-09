import re
import math

def lcm(a, b):
  return abs(a*b) // math.gcd(a, b)

def lcm_multiples(numbers):
  multiple = numbers[0]
  for number in numbers[1:]:
    multiple = lcm(multiple, number)
  return multiple

def main():
  f = open("./q8_input.txt", "r")

  directions = list(f.readline().strip())
  f.readline()

  elements = {}
  nodes = []
  for line in f:
    data = line.strip().split('=')
    direction_elements = re.findall("\w+", data[1])
    node = data[0].strip()
    elements[node] = (direction_elements[0], direction_elements[1])
    if node[2] == 'A':
      nodes.append(node)

  iters = []
  for i in range(len(nodes)):
    node = nodes[i]
    steps = 0
    while node[2] != 'Z':
      direction = 0 if directions[steps % len(directions)] == 'L' else 1
      node = elements[node][direction]
      steps += 1
    iters.append(steps)

  print(lcm_multiples(iters))

main()