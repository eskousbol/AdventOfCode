import copy

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
  f = open("./q10b_test_2_input.txt", "r")

  start_position = None
  grid = []
  for line in f:
    row = list(line.strip())
    grid.append(row)
    if 'S' in row:
      start_position = [len(grid) - 1, row.index('S')]

  grid_copy = copy.deepcopy(grid)
  current_cell = start_position
  done = False
  loop = [current_cell]
  while not done:
    adjacent_pipes = find_adjacent_pipes(grid, current_cell)
    added_pipes = False
    for pipe in adjacent_pipes:
      grid[current_cell[0]][current_cell[1]] = 'N'
      added_pipes = True
      current_cell = pipe
      loop.append(pipe)
      # On the first go around pick only one adjacent pipe so we choose a direction
      if len(loop) == 2:
        break
    if not added_pipes:
      done = True

  grid = grid_copy

  rows = {}
  for item in loop:
    row = item[0]
    col = item[1]
    pipe = grid[row][col]
    if pipe == '-':
      continue
    if row in rows.keys():
      rows[row].append(col)
    else:
      rows[row] = [col]
  
  for row in rows.keys():
    row_data = rows[row]
    row_data.sort()
    rows[row] = row_data

  """print( rows)
  contained_cells_count = 0
  for row in rows.keys():
    parity = True
    row_data = rows[row]
    for i in range(0, len(row_data) - 1, 2):
      distance = row_data[i + 1] - row_data[i]
      if grid[row][row_data[i] + 1] == '.':
        if distance > 1:
          print(parity, row, row_data, row_data[i + 1], row_data[i])
        contained_cells_count += distance - 1
      parity = not parity """

  contained_cells = []
  uncontained_cells = []
  for i in range(len(grid)):
    row = grid[i]
    for j in range(len(row)):
      item = row[j]
      if item == '.':
        if blocked_below(grid, [i, j]) and blocked_right(grid, [i, j]) and blocked_above(grid, [i, j]) and blocked_left(grid, [i, j]):
          print(row, [i,j])
          contained_cells.append([i,j])
        else:
          uncontained_cells.append([i,j])
  
  print(contained_cells)
  for [i, j] in uncontained_cells:
    row = grid[i]
    # If it is not a contained cell, make sure all its adjacent neighbours are cleaned out since they are also not contained
    k = 1
    while j + k < len(row) and row[j + k] == '.':
      [i, j + k] in contained_cells and contained_cells.remove([i, j + k])
      k += 1
    k = 1
    while j - k > 0 and row[j - k] == '.':
      [i, j - k] in contained_cells and contained_cells.remove([i, j - k])
      k += 1
    k = 1
    while i + k < len(grid) and grid[i+k][j] == '.':
      [i + k, j] in contained_cells and contained_cells.remove([i + k, j])
      k += 1
    k = 1
    while i - k > 0 and grid[i-k][j] == '.':
      [i - k, j] in contained_cells and contained_cells.remove([i - k, j])
      k += 1

  print(contained_cells)
  print(len(contained_cells))

def blocked_above(grid, current_cell):
  for i in range(0, current_cell[0]):
    if grid[current_cell[0] - i][current_cell[1]] == '-':
      return True
  return False

def blocked_right(grid, current_cell):
  for i in range(current_cell[1], len(grid[current_cell[0]])):
    if grid[current_cell[0]][i] == '|':
      return True
  return False

def blocked_below(grid, current_cell):
  for i in range(current_cell[0], len(grid)):
    if grid[i][current_cell[1]] == '-':
      return True
  return False

def blocked_left(grid, current_cell):
  for i in range(0, current_cell[1]):
    if grid[current_cell[0]][current_cell[1] - i] == '|':
      return True
  return False



main()