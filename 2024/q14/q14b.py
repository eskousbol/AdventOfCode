import re
from datetime import datetime

GRID_HEIGHT = 103
GRID_WIDTH = 101

SECONDS = 10000

def move(position, velocity):
  return [((position[0] + velocity[0]) % GRID_HEIGHT), ((position[1] + velocity[1]) % GRID_WIDTH)]

def draw_grid(grid):
  for row in grid:
    new_row = ''
    for item in row:
      new_row += str(item)
    print(new_row)

def is_full_line(grid):
  for row in grid:
    if '#' * 10 in ''.join(row):
      return True
  return False

def main():
  start = datetime.now()
  f = open("./q14_input.txt", "r")

  robots = []
  for line in f:
    match = re.search("p=((-?\d+),(-?\d+)) v=((-?\d+),(-?\d+))", line)
    pos = [int(match.group(3)), int(match.group(2))]
    vel = [int(match.group(6)), int(match.group(5))]
    robots.append([pos, vel])

  seconds = 0
  for i in range(SECONDS):
    grid = [['.'] * GRID_WIDTH for y in range(GRID_HEIGHT)]

    for robot in robots:
      new_position = move(robot[0], robot[1])
      grid[new_position[0]][new_position[1]] = '#'
      robot[0] = new_position

    if is_full_line(grid):
      end = datetime.now()
      seconds = i + 1
      print('-------------------')
      print('s=' + str(i + 1))
      draw_grid(grid)
      print('-------------------')
      break
  
  
  diff = end - start
  print(diff)
  print(seconds)


main()