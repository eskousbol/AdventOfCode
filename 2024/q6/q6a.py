def on_board(grid, position):
  if position[0] < 0:
    return False
  if position[1] < 0:
    return False
  if position[0] >= len(grid[0]):
    return False
  if position[1] >= len(grid):
    return False
  return True

def main():
  f = open("./q6_test_input.txt", "r")

  grid = []
  position = None
  j = 0
  for line in f:
    row = list(line.strip())
    grid.append(row)
    if '^' in row:
      position = (j, row.index('^'))
    j += 1

  
  unique_spots = 1 # 1 to account for the start space
  direction = (-1, 0)
  done = False
  while not done:
    proposed_position = (position[0] + direction[0], position[1] + direction[1])
    if not on_board(grid, proposed_position):
      done = True
      break
    if grid[proposed_position[0]][proposed_position[1]] == '#':
      direction = (direction[1], -direction[0])
    else:
      if grid[proposed_position[0]][proposed_position[1]] == '.':
        grid[proposed_position[0]][proposed_position[1]] = 'X'
        unique_spots += 1
      position = proposed_position
  
  print(unique_spots)

main()