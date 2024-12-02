class Path:
  def __init__(self, x, y, d_x, d_y, straight):
    self.x = x
    self.y = y
    self.d_x = d_x
    self.d_y = d_y
    self.straight = straight

  def to_string(self):
    return f"{self.x},{self.y},{self.d_x},{self.d_y}"

  def find_options(self, max_x, max_y):
    options = [] 
    if self.straight != 3 and self.x + self.d_x <= max_x and self.x + self.d_x >= 0 and self.y + self.d_y <= max_y and self.y + self.d_y >= 0:
      options.append(Path(self.x + self.d_x, self.y + self.d_y, self.d_y, self.d_x, self.straight + 1))
    if self.d_x == 0:
      if self.x + 1 <= max_x:
        options.append(Path(self.x + 1, self.y, 1, 0, 0))
      if self.x - 1 >= 0:
        options.append(Path(self.x - 1, self.y, -1, 0, 0))
    else:
      if self.y + 1 <= max_y:
        options.append(Path(self.x, self.y + 1, 0, 1, 0))
      if self.y - 1 >= 0:
        options.append(Path(self.x, self.y - 1, 0, -1, 0))
    return options


def follow_path(grid, x, y , d_x, d_y, paths, heat_loss):
  while x !=  len(grid[0]) - 1 and y != len(grid) - 1:
    path = Path(x, y, d_x, d_y, 0)
    if path.to_string() in paths:
      return heat_loss
    heat_loss += int(grid[y][x])
    paths.append(path.to_string())
    options = path.find_options(len(grid[0]) - 1, len(grid) - 1)
    for option in options:
      heat_loss += follow_path(grid, option.x, option.y, option.d_x, option.d_y, paths, heat_loss)
    print(x,y, heat_loss)
    x += d_x
    y += d_y
  return heat_loss

def main():
  f = open("./q17_test_input.txt", "r")

  grid = []
  for line in f:
    grid.append(list(line.strip()))
  
  x = 0
  y = 0
  d_x = 1
  d_y = 0
  energized_grid = follow_path(grid, x, y , d_x, d_y, [], 0)

  for line in energized_grid:
    energized_cells += line.count('#')
  print(energized_cells)

main()