from datetime import datetime
DIRECTIONS = {
  '>': (0, 1),
  '^': (-1, 0),
  '<': (0, -1),
  'v': (1, 0)
}

def flatten(xss):
  return [x for xs in xss for x in xs]

def get_grid():
  f = open("./q15_input.txt", "r")

  grid_done = False
  grid = []
  directions = []
  start_position = None
  i = 0
  for line in f:
    if grid_done:
      directions.append(list(line.strip()))
    else:
      chars = list(line.strip())
      if len(chars) > 0:
        if '@' in chars:
          start_position = (i,chars.index('@'))
        grid.append(chars)
        i += 1
      else:
        grid_done = True
  return [grid, flatten(directions), start_position]

def move(direction, position):
  return (position[0] + direction[0], position[1] + direction[1])

def get_item_at_position(grid, position):
  return grid[position[0]][position[1]]

def set_item_at_position(grid, position, value):
  grid[position[0]][position[1]] = value

def move_item(grid, position, direction):
  proposed_position = move(DIRECTIONS[direction], position)
  proposed_position_item = get_item_at_position(grid, proposed_position)
  position_item = get_item_at_position(grid, position)

  if proposed_position_item == '.':
    set_item_at_position(grid, position, proposed_position_item)
    set_item_at_position(grid, proposed_position, position_item)
    position = proposed_position
  elif proposed_position_item == 'O':
    [grid, throwaway] = move_item(grid, proposed_position, direction)
    proposed_position_item = get_item_at_position(grid, proposed_position)
    # if we were able to successfully move the item(s) blocking the path
    if get_item_at_position(grid, proposed_position) == '.':
      set_item_at_position(grid, position, proposed_position_item)
      set_item_at_position(grid, proposed_position, position_item)
      position = proposed_position
  # other case -- it's a wall, so we do nothing

  return [grid, position]

def print_grid(grid):
  for row in grid:
    print(''.join(row))

def sum_gps_coordinates(grid):
  sum = 0
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      item = grid[i][j]
      if item == 'O':
        sum += (100 * i) + j
  return sum

def main():
  start = datetime.now()
  [grid, directions, position] = get_grid()

  for direction in directions:
    [grid, position] = move_item(grid, position, direction)

  result = sum_gps_coordinates(grid)
  end = datetime.now()

  diff = end - start
  print(diff)
  print(result)

main()