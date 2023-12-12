def main():
  f = open("./q11_input.txt", "r")

  universe = []
  # Basic universe
  for line in f:
    row = list(line.strip())
    universe.append(row)  

  # Find all the empty rows
  spare_rows = []
  for i in range(len(universe)):
    row = universe[i]
    if '#' not in row:
      spare_rows.append(i)
  spare_rows.sort(reverse=True)

  # Then the empty columns
  spare_cols = []
  universe_transpose = list(zip(*universe))
  for j in range(len(universe_transpose)):
    col = universe_transpose[j]
    if '#' not in col:
      spare_cols.append(j)
  spare_cols.sort(reverse=True)

  # Expand
  for i in range(len(universe)):
    for col in spare_cols:
      universe[i].insert(col, 'O')
  
  for row in spare_rows:
    universe.insert(row, ['O'] * len(universe[0]))
  
  # Find galaxies
  galaxies = []
  for i in range(len(universe)):
    row = universe[i]
    indices = [j for j, x in enumerate(row) if x == "#"]
    for index in indices:
      galaxies.append([i, index])

  order = 999999
  path_length_sum = 0

  # Count shortest paths sum
  for i in range(len(galaxies)):
    galaxy_1 = galaxies[i]
    for j in range(len(galaxies)):
      if i <= j:
        continue
      galaxy_2 = galaxies[j]

      row_distance = 0
      col_distance = 0

      y_distance = abs(galaxy_2[0] - galaxy_1[0])
      min_y = min(galaxy_1[0], galaxy_2[0])
      x_distance = abs(galaxy_2[1] - galaxy_1[1])
      min_x = min(galaxy_1[1], galaxy_2[1])

      for step in range(min_x, min_x + x_distance):
        if universe[min_y][step] == 'O':
          row_distance += order
        else:
          row_distance += 1
      for step in range(min_y, min_y + y_distance):
        if universe[step][min_x] == 'O':
          col_distance += order
        else:
          col_distance += 1
      path_length_sum += row_distance + col_distance

  print(path_length_sum)

main()