def check_vertical(grid):
  grid_transpose = list(zip(*grid))
  return check_horizontal(grid_transpose)

def check_horizontal(grid):
  last_line = None
  for i in range(len(grid)):
    line = grid[i]
    if last_line and last_line == ''.join(line):
      if verify_reflection_line(grid, i - 1):
        return i
    last_line = ''.join(line)
  return None

def verify_reflection_line(grid, line_number):
  reflects = True
  for i in range(len(grid) // 2):
    if line_number - i >= 0 and line_number + 1 + i < len(grid):
      if grid[line_number - i] != grid[line_number + 1 + i]:
        reflects = False
  return reflects

def main():
  f = open("./q13_input.txt", "r")

  total = 0
  grid = []
  for line in f:
    if len(line.strip()) == 0:
      vertical_line = check_vertical(grid)
      if vertical_line:
        total += vertical_line
      horizontal_line = check_horizontal(grid)
      if horizontal_line:
        total += horizontal_line * 100
      grid = []
      continue
    grid.append(list(line.strip()))

  # For the last grid parsed
  vertical_line = check_vertical(grid)
  if vertical_line:
    total += vertical_line
  horizontal_line = check_horizontal(grid)
  if horizontal_line:
    total += horizontal_line * 100
  grid = []

  print(total)

main()