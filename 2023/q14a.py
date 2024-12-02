import re

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

def main():
  f = open("./q14_input.txt", "r")

  grid = []
  for line in f:
    grid.append(list(line.strip()))

  grid = tilt_north(grid)

  total = 0
  for i in range(len(grid)):
    line = grid[i]
    rocks = re.findall("O", "".join(line))
    multiplier = len(grid) - i
    total += len(rocks) * multiplier
  print(total)

main()