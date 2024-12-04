def main():
  f = open("./q4_input.txt", "r")

  grid = []
  mirror = []
  for line in f:
    grid.append(line.strip())

  total = 0

  for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[i]) -1):
      if grid[i][j] == "A":
        cross_matches = 0
        if grid[i -1][j - 1] == "S":
          if grid[i+1][j+1] == "M":
            cross_matches += 1
        if grid[i - 1][j + 1] == "S":
          if grid[i+1][j - 1] == "M":
            cross_matches += 1
        if grid[i + 1][j - 1] == "S":
          if grid[i - 1][j + 1] == "M":
            cross_matches += 1
        if grid[i + 1][j + 1] == "S":
          if grid[i - 1][j - 1] == "M":
            cross_matches += 1
        if cross_matches >= 2:
          total += 1
  print(total)

main()