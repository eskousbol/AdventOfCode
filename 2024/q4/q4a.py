import re
def get_diagonal_1(grid):
  # top left to bottom right
  diagonal_1_grid = []
  for i in range(len(grid)):
    row = []
    for j in range(len(grid[i]) - i):
      if ( i+j < len(grid)):
        row.append(grid[i + j][j])
    diagonal_1_grid.append(''.join(row))

  for i in range(1,len(grid)):
    row = []
    for j in range(len(grid[i]) - i):
      row.append(grid[j][i+j])
    diagonal_1_grid.append(''.join(row))

  return '|'.join(diagonal_1_grid)

def main():
  f = open("./q4_input.txt", "r")

  grid = []
  mirror = []
  for line in f:
    grid.append(line.strip())
    mirror.append(line.strip()[::-1])

  horizontal_grid = '|'.join(grid)

  transpose = zip(*grid)
  transpose = [''.join(value for value in row) for row in transpose ]
  vertical_grid = '|'.join(transpose)

  diagonal_1_grid = get_diagonal_1(grid)
  diagonal_2_grid = get_diagonal_1(mirror)

  all_grids = '|'.join([vertical_grid, horizontal_grid,  diagonal_1_grid, diagonal_2_grid])
  xmas_matches = re.findall("XMAS", all_grids)
  samx_matches = re.findall("SAMX", all_grids)

  print(len(xmas_matches) + len(samx_matches))


main()