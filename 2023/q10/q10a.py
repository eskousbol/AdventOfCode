def check_top_is_adjacent_pipe(current_cell, adjacent_cell):
  accepted_cells = ['F', '|', '7']
  if current_cell == 'S':
    if adjacent_cell in accepted_cells:
      return True
  elif current_cell == '|':
    if adjacent_cell in accepted_cells:
      return True
  elif current_cell == 'J':
    if adjacent_cell in accepted_cells:
      return True
  elif current_cell == 'L':
    if adjacent_cell in accepted_cells:
      return True
  return False

def check_right_is_adjacent_pipe(current_cell, adjacent_cell):
  accepted_cells = ['-', 'J', '7']
  if current_cell == 'S':
    if adjacent_cell in accepted_cells:
      return True
  elif current_cell == '-':
    if adjacent_cell in accepted_cells:
      return True
  elif current_cell == 'F':
    if adjacent_cell in accepted_cells:
      return True
  elif current_cell == 'L':
    if adjacent_cell in accepted_cells:
      return True
  return False

def check_bottom_is_adjacent_pipe(current_cell, adjacent_cell):
  accepted_cells = ['L', '|', 'J']
  if current_cell == 'S':
    if adjacent_cell in accepted_cells:
      return True
  elif current_cell == '|':
    if adjacent_cell in accepted_cells:
      return True
  elif current_cell == '7':
    if adjacent_cell in accepted_cells:
      return True
  elif current_cell == 'F':
    if adjacent_cell in accepted_cells:
      return True
  return False

def check_left_is_adjacent_pipe(current_cell, adjacent_cell):
  accepted_cells = ['-', 'L', 'F']
  if current_cell == 'S':
    if adjacent_cell in accepted_cells:
      return True
  elif current_cell == '-':
    if adjacent_cell in accepted_cells:
      return True
  elif current_cell == 'J':
    if adjacent_cell in accepted_cells:
      return True
  elif current_cell == '7':
    if adjacent_cell in accepted_cells:
      return True
  return False

# Returns an array of pipes that connect to this pipe
def find_adjacent_pipes(grid, current_cell):
  adjacent_pipes = []
  # Top
  if current_cell[0] > 0 and check_top_is_adjacent_pipe(grid[current_cell[0]][current_cell[1]], grid[current_cell[0] - 1][current_cell[1]]):
    adjacent_pipes.append([current_cell[0] - 1, current_cell[1]])
  # Right
  if current_cell[1] < len(grid[current_cell[0]]) - 1 and check_right_is_adjacent_pipe(grid[current_cell[0]][current_cell[1]], grid[current_cell[0]][current_cell[1] + 1]):
    adjacent_pipes.append([current_cell[0], current_cell[1] + 1])
  # Bottom
  if current_cell[0] < len(grid) - 1 and check_bottom_is_adjacent_pipe(grid[current_cell[0]][current_cell[1]], grid[current_cell[0] + 1][current_cell[1]]):
    adjacent_pipes.append([current_cell[0] + 1, current_cell[1]])
  # Left
  if current_cell[1] > 0 and check_left_is_adjacent_pipe(grid[current_cell[0]][current_cell[1]], grid[current_cell[0]][current_cell[1] - 1]):
    adjacent_pipes.append([current_cell[0], current_cell[1] - 1])

  return adjacent_pipes

def main():
  f = open("./q10_input.txt", "r")

  start_position = None
  grid = []
  for line in f:
    row = list(line.strip())
    grid.append(row)
    if 'S' in row:
      start_position = [len(grid) - 1, row.index('S')]

  grid_copy = grid
  current_cell = start_position
  done = False
  loop = [current_cell]
  while not done:
    adjacent_pipes = find_adjacent_pipes(grid, current_cell)
    added_pipes = False
    for pipe in adjacent_pipes:
      grid_copy[current_cell[0]][current_cell[1]] = 'N'
      added_pipes = True
      current_cell = pipe
      loop.append(pipe)
      # On the first go around pick only one adjacent pipe so we choose a direction
      if len(loop) == 2:
        break
    if not added_pipes:
      done = True
  print(len(loop) // 2)

main()