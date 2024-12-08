import math

def calculate_directions(position_1, position_2):
  return [position_1[0] - position_2[0], position_1[1] - position_2[1]]

def calculate_euclidean_distance(position_1, position_2):
  return math.sqrt((position_1[0] - position_2[0])**2 + (position_1[1] - position_2[1])**2)

def update_position(direction, position):
  return (position[0] + direction[0], position[1] + direction[1])

def is_valid_antinode(antenna_1, antenna_2, antinode):
  antenna_1_distance = calculate_euclidean_distance(antenna_1, antinode)
  antenna_2_distance = calculate_euclidean_distance(antenna_2, antinode)
  if antenna_1_distance == 2 * antenna_2_distance:
    return True
  return antenna_2_distance == 2 * antenna_1_distance

def on_grid(position, grid_width, grid_height):
  if position[0] < 0:
    return False
  if position[1] < 0:
    return False
  if position[0] >= grid_height:
    return False
  if position[1] >= grid_width:
    return False
  return True

def main():
  f = open("./q8_input.txt", "r")

  antennae = {}
  grid_height = 0
  grid_width = 0
  for line in f:
    row = list(line.strip())
    grid_width = len(row)
    for i in range(len(row)):
      if row[i] != '.':
        if row[i] in antennae.keys():
          antennae[row[i]].append((grid_height, i))
        else:
          antennae[row[i]] = []
          antennae[row[i]].append((grid_height, i))
    grid_height += 1

  antinodes = set()
  for frequency in antennae.keys():
    positions = antennae[frequency]
    for i in range(len(positions) - 1):
      antenna_1 = positions[i]
      antinodes.add(antenna_1)
      for j in range(i + 1, len(positions)):
        antenna_2 = positions[j]
        antenna_directions = calculate_directions(antenna_1, antenna_2)
        antinode = update_position(antenna_1, antenna_directions)
        while on_grid(antinode, grid_width, grid_height):
          antinodes.add(antinode)
          antinode = update_position(antinode, antenna_directions)

        antenna_directions = [-antenna_directions[0], -antenna_directions[1]]
        antinode = update_position(antenna_1, antenna_directions)
        while on_grid(antinode, grid_width, grid_height):
          antinodes.add(antinode)
          antinode = update_position(antinode, antenna_directions)


  print(len(antinodes))

main()