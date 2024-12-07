def on_board(grid, position):
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

def calculate_direction(direction):
  if direction[0] == 1:
    return 'D'
  if direction[0] == -1:
    return 'U'
  if direction[1] == 1:
    return 'R'
  return 'L'

def update_traversed_squares(traversed_squares, position, direction):
  y = position[0]
  x = position[1]
  if y in traversed_squares.keys():
    if x in traversed_squares[y].keys():
      traversed_squares[y][x].add(calculate_direction(direction))
    else:
      traversed_squares[y][x] = set(calculate_direction(direction))
  else:
    traversed_squares[y] = { x: set(calculate_direction(direction))}
  return traversed_squares

# Case 1 -- we have already been on the desired square in the same direction we will be going
def check_same_direction(traversed_squares, position, direction):
    y = position[0]
    x = position[1]

    current_direction = calculate_direction(direction)

    if y in traversed_squares.keys():
      if x in traversed_squares[y].keys():
        #print(position, direction, traversed_squares[y][x])
        if current_direction in traversed_squares[y][x]:
          return True
    return False

# Case 2 -- we can get to a square we've already been on in the same direction without turning
def current_position(grid, traversed_squares, position, direction):
    current_direction = calculate_direction(direction)
    current_position = (position[0], position[1])
    done = False
    while on_board(grid, current_position) and not done:
      y = current_position[0]
      x = current_position[1]
      if y in traversed_squares.keys():
        if x in traversed_squares[y].keys():
          #print(position, direction, traversed_squares[y][x])
          if current_direction in traversed_squares[y][x]:
            done = True
      if not done:
        current_position = move(direction, current_position)
    return done

# Case 3 -- position where the guard turns 180 degrees
def loop_conditions(grid, traversed_squares, position, direction):
  turned_right_direction = turn_right(direction)
  in_front_position = move(direction, position)
  turned_right_position = move(turned_right_direction, position)
  if on_board(grid, in_front_position) and grid[in_front_position[0]][in_front_position[1]] == '#':
    if on_board(grid, turned_right_position) and grid[turned_right_position[0]][turned_right_position[1]] == '#':
      # Could potentially be a loop -- go back the way we have and see if we find the same thing
      return set(in_front_position, turned_right_position)
    return set(in_front_position)
  elif on_board(grid, turned_right_position) and grid[turned_right_position[0]][turned_right_position[1]] == '#':
    return set(turned_right_position)
  return ()

def loop_180(grid, traversed_squares, position, direction):
  current_direction = calculate_direction(direction)
  current_position = (position[0], position[1])
  done = False
  turned_right_direction = turn_right(direction)
  loop_count = 0
  loops_found = 0
  while on_board(grid, current_position) and not done:
    blocked_spots = loop_conditions(grid, traversed_squares, position, direction)
    loop_count += len(blocked_spots)
    if loop_count > 0 and loops_found == 0:
      loops_found += 1
      # Could potentially be a loop -- go back the way we have and see if we find the same thing
      direction = turn_right(turned_right_direction)
    elif loop_count > 0 and loops_found > 0:
      print(loop_count)
      done = True
    if not done:
      current_position = move(direction, current_position)
  return done

def main():
  f = open("./q6_test_input.txt", "r")

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
  traversed_squares = {}
  obstructions = set()
  while not done:
    proposed_position = move(direction, position)
    if not on_board(grid, proposed_position):
      done = True
      break
    if grid[proposed_position[0]][proposed_position[1]] == '#':
      traversed_squares = update_traversed_squares(traversed_squares, position, direction)
      direction = turn_right(direction)
    else:
      # Check if we turn to the right, will we be on a square we have already been on, in a direction we have already travelled in
      turned_right_direction = turn_right(direction)
      turned_right_position = move(turned_right_direction, position)
      if on_board(grid, turned_right_position):
        if (check_same_direction(traversed_squares, turned_right_position, turned_right_direction)):
          obstructions.add(proposed_position)
        elif (current_position(grid, traversed_squares, turned_right_position, turned_right_direction)):
          obstructions.add(proposed_position)
        elif(loop_180(grid, traversed_squares, turned_right_position, turned_right_direction)):
          loop_position = loop_180(grid, traversed_squares, turned_right_position, turned_right_direction)
          obstructions.add(loop_position)

      # Mark where we've been with what direction we have travelled
      traversed_squares = update_traversed_squares(traversed_squares, position, direction)
      position = proposed_position
  
  print(len(obstructions))
  print(obstructions)
  # (9, 7), (8, 3), (8, 1), (7,7), (7, 6), (6, 3)
  #print(len(obstructions.intersection(set([(9, 7), (8, 3), (8, 1), (7,7), (7, 6), (6, 3)]))) == 6 and len(obstructions) == 6)

main()