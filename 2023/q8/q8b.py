import re

def all_end_nodes(nodes):
  for node in nodes:
    if node[2] != 'Z':
      return False
  return True

def main():
  f = open("./q8_input.txt", "r")

  directions = list(f.readline().strip())
  print(directions)
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

  steps = 0
  iter = 0
  while not all_end_nodes(nodes):
    if iter == len(directions):
      iter = 0
    direction = 0 if directions[iter] == 'L' else 1
    new_nodes = []
    for i in range(len(nodes)):
      new_nodes.append(elements[nodes[i]][direction])
    steps += 1
    iter += 1
    nodes = new_nodes
    if steps % 10000 == 0:
      print(nodes)
  print(steps)
  

main()