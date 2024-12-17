
searched_regions = set()

def find_neighbours(grid, position):
  edges = set()
  area = 1
  plot_perimeter = 4

  i = position[0]
  j = position[1]
  if str(i) + '|' + str(j) in searched_regions:
    return [0, []]

  plot = grid[i][j]

  searched_regions.add(str(i) + '|' + str(j))

  if i - 1 >= 0 and grid[i - 1][j] == plot:
    plot_perimeter -= 1
    [a1, e1] = find_neighbours(grid, [i-1, j])
    area += a1
    edges = edges.union(e1)

  if i + 1 < len(grid) and grid[i + 1][j] == plot:
    plot_perimeter -= 1
    [a1, e1] = find_neighbours(grid, [i+1, j])
    area += a1
    edges = edges.union(e1)

  if j - 1 >= 0 and grid[i][j - 1] == plot:
    plot_perimeter -= 1
    [a1, e1] = find_neighbours(grid, [i, j -1])
    area += a1
    edges = edges.union(e1)
  
  if j + 1 < len(grid[0]) and grid[i][j + 1] == plot:
    plot_perimeter -= 1
    [a1, e1] = find_neighbours(grid, [i, j + 1])
    area += a1
    edges = edges.union(e1)

  if (plot_perimeter > 0):
    edges.add(str(i) + '|' + str(j))
  return [area, edges]


def main():
  #f = open("./q12_input.txt", "r")

  f = [
    'AAAA',
    'BBCD',
    'BBCC',
    'EEEC'
  ]
  grid = []
  for line in f:
    grid.append(list(line.strip()))

  result = 0
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      [area, edges] = find_neighbours(grid, [i,j])
      result += area * 1

  print(result)

main()