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
          if current_direction in traversed_squares[y][x]:
            done = True
      if not done:
        current_position = move(direction, current_position)
    return done

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

      # Mark where we've been with what direction we have travelled
      traversed_squares = update_traversed_squares(traversed_squares, position, direction)
      position = proposed_position
  
  print(len(obstructions))
main()