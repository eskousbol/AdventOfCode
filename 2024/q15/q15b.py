from datetime import datetime
from copy import deepcopy
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
        new_chars = list(chars)
        new_chars = ''
        for item in chars:
          if item == '#':
            new_chars += '##'
          elif item == 'O':
            new_chars += '[]'
          elif item == '.':
            new_chars += '..'
          elif item == '@':
            new_chars += '@.'

        new_chars = list(new_chars)
        if '@' in new_chars:
          start_position = (i,new_chars.index('@'))
        grid.append(new_chars)
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

def move_block_item(grid, direction, proposals):
  if direction in ['^', 'v'] and proposals['left_proposed_position_item'] == '.' and proposals['right_proposed_position_item'] == '.':
    set_item_at_position(grid, proposals['left_position'], proposals['left_proposed_position_item'])
    set_item_at_position(grid, proposals['left_proposed_position'], proposals['left_position_item'])

    set_item_at_position(grid, proposals['right_position'], proposals['right_proposed_position_item'])
    set_item_at_position(grid, proposals['right_proposed_position'], proposals['right_position_item'])

  elif direction == '<' and proposals['left_proposed_position_item'] == '.':
    set_item_at_position(grid, proposals['left_position'], proposals['right_position_item'])
    set_item_at_position(grid, proposals['left_proposed_position'], proposals['left_position_item'])

    set_item_at_position(grid, proposals['right_position'], '.')

  elif direction == '>' and proposals['right_proposed_position_item'] == '.':
    set_item_at_position(grid, proposals['left_position'], '.')

    set_item_at_position(grid, proposals['right_position'], proposals['left_position_item'])
    set_item_at_position(grid, proposals['right_proposed_position'], proposals['right_position_item'])
  return grid

def move_single_item(grid, position, direction):
  proposed_position = move(DIRECTIONS[direction], position)
  proposed_position_item = get_item_at_position(grid, proposed_position)
  position_item = get_item_at_position(grid, position)

  if proposed_position_item == '.':
    set_item_at_position(grid, position, proposed_position_item)
    set_item_at_position(grid, proposed_position, position_item)
    position = proposed_position
  elif proposed_position_item in ['[', ']']:
    [new_grid, throwaway] = move_item(deepcopy(grid), proposed_position, direction)
    proposed_position_item = get_item_at_position(new_grid, proposed_position)
    # if we were able to successfully move the item(s) blocking the path
    if proposed_position_item == '.':
      grid = new_grid
      set_item_at_position(grid, position, '.')
      set_item_at_position(grid, proposed_position, position_item)
      position = proposed_position
  # other case -- it's a wall, so we do nothing

  return [grid, position]

# position should always be the left most position of the object we are moving
def move_item(grid, position, direction):
  position_item = get_item_at_position(grid, position)
  # things we can treat as singles
  if position_item == '@':
    return move_single_item(grid, position, direction)
  elif position_item == '#' or position_item == '.':
    return [grid, position]

  # OTHERWISE start dealing with the double wides (i.e. the blocks [])
  left_position = position if position_item == '[' else move(DIRECTIONS['<'], position)
  right_position = move(DIRECTIONS['>'], left_position)

  left_position_item = get_item_at_position(grid, left_position)
  right_position_item = get_item_at_position(grid, right_position)

  left_proposed_position = move(DIRECTIONS[direction], left_position)
  right_proposed_position = move(DIRECTIONS['>'], left_proposed_position)
  
  left_proposed_position_item = get_item_at_position(grid, left_proposed_position)
  right_proposed_position_item = get_item_at_position(grid, right_proposed_position)

  proposals = {
    'left_position': left_position,
    'right_position': right_position,
    'left_position_item': left_position_item,
    'right_position_item': right_position_item,
    'left_proposed_position': left_proposed_position,
    'right_proposed_position': right_proposed_position,
    'left_proposed_position_item': left_proposed_position_item,
    'right_proposed_position_item': right_proposed_position_item
  }

  # If there is a blocker in front of us do nothing
  if left_proposed_position_item == '#' or right_proposed_position_item == '#':
    return [grid, position]
  # Simple cases -- we have an empty spce where we want to go
  if direction in ['^', 'v'] and left_proposed_position_item == '.' and right_proposed_position_item == '.':
    grid = move_block_item(grid, direction, proposals)
    position = left_proposed_position
  elif direction == '<' and left_proposed_position_item == '.':
    grid = move_block_item(grid, direction, proposals)
    position = left_proposed_position
  elif direction == '>' and right_proposed_position_item == '.':
    grid = move_block_item(grid, direction, proposals)
    position = left_proposed_position
  # Complex case -- there is another block in our path
  elif direction == '>':
    [grid, throwaway] = move_item(grid, right_proposed_position, direction)

    left_proposed_position_item = get_item_at_position(grid, left_proposed_position)
    right_proposed_position_item = get_item_at_position(grid, right_proposed_position)

    proposals['left_proposed_position_item'] = left_proposed_position_item
    proposals['right_proposed_position_item'] = right_proposed_position_item
    if right_proposed_position_item == '.':
      grid = move_block_item(grid, direction, proposals)
      position = right_proposed_position
  
  elif direction == '<':
    [grid, throwaway] = move_item(grid, left_proposed_position, direction)

    left_proposed_position_item = get_item_at_position(grid, left_proposed_position)
    right_proposed_position_item = get_item_at_position(grid, right_proposed_position)

    proposals['left_proposed_position_item'] = left_proposed_position_item
    proposals['right_proposed_position_item'] = right_proposed_position_item
    if left_proposed_position_item == '.':
      grid = move_block_item(grid, direction, proposals)
      position = left_proposed_position

  elif direction == '^' or direction == 'v':
    [grid, throwaway] = move_item(grid, left_proposed_position, direction)
    [grid, throwaway] = move_item(grid, right_proposed_position, direction)
    
    left_proposed_position_item = get_item_at_position(grid, left_proposed_position)
    right_proposed_position_item = get_item_at_position(grid, right_proposed_position)

    proposals['left_proposed_position_item'] = left_proposed_position_item
    proposals['right_proposed_position_item'] = right_proposed_position_item
    if left_proposed_position_item == '.' and right_proposed_position_item == '.':
      grid = move_block_item(grid, direction, proposals)
      position = left_proposed_position

  return [grid, position]

def print_grid(grid):
  for row in grid:
    print(''.join(row))

def sum_gps_coordinates(grid):
  sum = 0
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      item = grid[i][j]
      if item == '[':
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