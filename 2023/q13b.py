def check_vertical(grid):
  grid_transpose = list(zip(*grid))
  return check_horizontal(grid_transpose)

def check_horizontal(grid):
  last_line = None
  for i in range(len(grid)):
    line = grid[i]
    if last_line:
      if (last_line and last_line == ''.join(line)) or count_differences(line, last_line) == 1:
        if verify_reflection_line(grid, i - 1):
          return i
        grid[i] = line
    last_line = ''.join(line)
  return None

def verify_reflection_line(grid, line_number):
  reflects = True
  total_differences = 0
  for i in range(len(grid) // 2):
    if line_number - i >= 0 and line_number + 1 + i < len(grid):
      line_1 = grid[line_number - i]
      line_2 = grid[line_number + i + 1]
      differences = count_differences(line_1, line_2)
      total_differences += differences
      if line_1 != line_2 and differences != 1:
        reflects = False
  if total_differences != 1:
    return False
  return reflects

def count_differences(line_1, line_2):
  differences = 0
  for i in range(len(line_1)):
    if line_1[i] != line_2[i]:
      differences += 1
  return differences

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