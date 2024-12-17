from copy import deepcopy

def on_grid(grid, position):
  if position[0] < 0:
    return False
  if position[1] < 0:
    return False
  if position[0] >= len(grid):
    return False
  if position[1] >= len(grid[0]):
    return False
  return True

def turn_right(direction):
  return (direction[1], -direction[0])

def move(direction, position):
  return (position[0] + direction[0], position[1] + direction[1])

def is_loop(grid, position, direction, obstruction_position):
  grid = deepcopy(grid)
  position = deepcopy(position)
  direction = deepcopy(direction)
  obstruction_position = deepcopy(obstruction_position)

  iterations = 0
  grid[obstruction_position[0]][obstruction_position[1]] = '#'
  max_iterations = 500000
  leaves_board = False
  while iterations < max_iterations:
    proposed_position = move(direction, position)
    if not on_grid(grid, proposed_position):
      leaves_board = True
      break

    if grid[proposed_position[0]][proposed_position[1]] == '#':
      direction = turn_right(direction)
    else:
      position = proposed_position
      iterations += 1
  grid[obstruction_position[0]][obstruction_position[1]] = '.'
  return not leaves_board
  
def main():
  f = open("./q6_input.txt", "r")

  grid = []
  position = None
  j = 0
  for line in f:
    row = list(line.strip())
    grid.append(row)
    if '^' in row:
      position = (j, row.index('^'))
    j += 1

  direction = (-1, 0)
  done = False
  obstructions = set()
  while not done:
    proposed_position = move(direction, position)
    if not on_grid(grid, proposed_position):
      done = True
      break

    if grid[proposed_position[0]][proposed_position[1]] == '#':
      direction = turn_right(direction)
    else:
      if is_loop(grid, position, direction, proposed_position):
        obstructions.add(str(proposed_position[0]) + ',' + (str(proposed_position[1])))
      position = proposed_position
  
  #print(len(obstructions.intersection(set([(9, 7), (8, 3), (8, 1), (7,7), (7, 6), (6, 3)]))) == 6 and len(obstructions) == 6)
  print(len(obstructions))

main()