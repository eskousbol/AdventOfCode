import copy

def follow_beam(grid, energized_grid, x, y , d_x, d_y, beams):
  while x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid):
    beam = f"{x},{y},{d_x},{d_y}"
    if beam in beams:
      return energized_grid
    beams.append(beam)
    energized_grid[y][x] = '#'
    if grid[y][x] == '\\':
      temp_d_x = d_x
      d_x = d_y
      d_y = temp_d_x
    elif grid[y][x] == '/':
      temp_d_x = d_x
      d_x = -d_y
      d_y = -temp_d_x
    elif grid[y][x] == '|':
      if d_x != 0:
        energized_grid = follow_beam(grid, energized_grid, x, y - d_x, 0, -d_x, beams)
        d_y = d_x
        d_x = 0
    elif grid[y][x] == '-':
      if d_y != 0:
        energized_grid = follow_beam(grid, energized_grid, x - d_y, y, -d_y, 0, beams)
        d_x = d_y
        d_y = 0
    x += d_x
    y += d_y
  return energized_grid

def main():
  f = open("./q16_input.txt", "r")

  grid = []
  energized_grid = []
  for line in f:
    grid.append(list(line.strip()))
    energized_grid.append(list('.' * len(line.strip())))
  
  x = 0
  y = 0
  d_x = 1
  d_y = 0

  max_energized_cells = 0
  for x in range(len(grid[0])):
    # Top row
    energized_cells = 0
    d_x = 0
    d_y = 1
    top_energized_grid = follow_beam(grid, copy.deepcopy(energized_grid), x, 0 , d_x, d_y, [])
    for line in top_energized_grid:
      energized_cells += line.count('#')
    if energized_cells > max_energized_cells:
      max_energized_cells = energized_cells
    
    # Bottom row
    energized_cells = 0
    d_x = 0
    d_y = -1
    bottom_energized_grid = follow_beam(grid, copy.deepcopy(energized_grid), x, len(grid) - 1, d_x, d_y, [])
    for line in bottom_energized_grid:
      energized_cells += line.count('#')
    if energized_cells > max_energized_cells:
      max_energized_cells = energized_cells
  
  for y in range(len(grid)):
    # Left column
    energized_cells = 0
    d_x = 1
    d_y = 0
    left_energized_grid = follow_beam(grid, copy.deepcopy(energized_grid), 0, y, d_x, d_y, [])
    for line in left_energized_grid:
      energized_cells += line.count('#')
    if energized_cells > max_energized_cells:
      max_energized_cells = energized_cells
    
    # Right column
    energized_cells = 0
    d_x = -1
    d_y = 0
    right_energized_grid = follow_beam(grid, copy.deepcopy(energized_grid), len(grid[0]) - 1, y, d_x, d_y, [])
    for line in right_energized_grid:
      energized_cells += line.count('#')
    if energized_cells > max_energized_cells:
      max_energized_cells = energized_cells
    
  print(max_energized_cells)

main()