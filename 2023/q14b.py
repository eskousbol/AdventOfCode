import re
def print_grid(grid):
  for line in grid:
    print(line)

def rotate_clockwise(grid):
  grid_transpose = list(zip(*grid[::-1]))
  new_grid = []
  for line in grid_transpose:
    new_grid.append(list(line))
  return new_grid

def tilt_north(grid):
  for i in range(len(grid)):
    line = grid[i]
    for j in range(len(line)):
      item = line[j]
      if item == 'O':
        k = i - 1
        while k >= 0 and grid[k][j] == '.':
          k -= 1
        if grid[k + 1][j] == '.':
          grid[k + 1][j] = item
          grid[i][j] = '.'
  return grid

def spin_cycle(grid):
  for i in range(4):
    grid = tilt_north(grid)
    grid = rotate_clockwise(grid)
  return grid

def count_load(grid):
  total = 0
  for i in range(len(grid)):
    line = grid[i]
    rocks = re.findall("O", "".join(line))
    multiplier = len(grid) - i
    total += len(rocks) * multiplier
  return total

def main():
  f = open("./q14_input.txt", "r")

  grid = []
  for line in f:
    grid.append(list(line.strip()))

  cycles = []
  cycle = []
  cycle_found = False
  start = 112
  for i in range(1000):
    grid = spin_cycle(grid)
    load = count_load(grid)
    if i >= start and not cycle_found:
      if len(cycle) > 1 and load == cycle[0]:
        cycles.append(cycle)
        cycle_found = True
        cycle = []
      cycle.append(load)

  cycle_to_calculate = 1000000000
  cycle_index = (cycle_to_calculate - start -1) % len(cycles[-1])
  print(cycles[-1][cycle_index])





  

main()