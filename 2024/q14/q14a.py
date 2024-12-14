import re

GRID_HEIGHT = 103
GRID_WIDTH = 101

SECONDS = 100

def find_final_position(position, velocity):
  for i in range(SECONDS):
    position = [((position[0] + velocity[0]) % GRID_HEIGHT), ((position[1] + velocity[1]) % GRID_WIDTH)]
  
  return position

def get_quadrant(position):
  middle_row = GRID_HEIGHT // 2
  middle_column = GRID_WIDTH // 2 
  if position[0] == middle_row:
    return None
  elif position[1] == middle_column:
    return None
  elif position[0] < middle_row and position[1] < middle_column:
    return 'TL'
  elif position[0] < middle_row and position[1] > middle_column:
    return 'TR'
  elif position[0] > middle_row and position[1] < middle_column:
    return 'BL'
  elif position[0] > middle_row and position[1] > middle_column:
    return 'BR'

def main():
  f = open("./q14_input.txt", "r")

  quadrant_counts = { 'TL': 0, 'TR': 0, 'BL': 0, 'BR': 0}
  grid =[['.' for x in range(GRID_WIDTH)] for y in range(GRID_HEIGHT)]
  for line in f:
    match = re.search("p=((-?\d+),(-?\d+)) v=((-?\d+),(-?\d+))", line)
    pos = [int(match.group(3)), int(match.group(2))]
    vel = [int(match.group(6)), int(match.group(5))]

    position = find_final_position(pos, vel)
    quadrant = get_quadrant(position)

    if(quadrant):
      quadrant_counts[quadrant] += 1

  result = quadrant_counts['TL'] * quadrant_counts['BL'] * quadrant_counts['TR'] * quadrant_counts['BR'] 

  print(result)


main()