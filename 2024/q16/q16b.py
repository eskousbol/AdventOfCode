from datetime import datetime

DIRECTIONS = {
  '>': (0, 1),
  '^': (-1, 0),
  '<': (0, -1),
  'v': (1, 0)
}

def get_maze():
  # f = open("./q16_input.txt", "r")

  f = [
    '###############',
    '#.......#....E#',
    '#.#.###.#.###.#',
    '#.....#.#...#.#',
    '#.###.#####.#.#',
    '#.#.#.......#.#',
    '#.#.#####.###.#',
    '#...........#.#',
    '###.#.#####.#.#',
    '#...#.....#.#.#',
    '#.#.#.###.#.#.#',
    '#.....#...#.#.#',
    '#.###.#.#.#.#.#',
    '#S..#.....#...#',
    '###############'
  ]
  maze = []
  start_position = None
  end_position = None
  i = 0
  for line in f:
    chars = list(line.strip())
    if 'S' in chars:
      start_position = (i,chars.index('S'))
    if 'E' in chars:
      end_position = (i,chars.index('E'))
    maze.append(chars)
    i += 1
  return [maze, start_position, end_position]

def move(direction, position):
  return (position[0] + direction[0], position[1] + direction[1])

def turn_right(direction):
  return (direction[1], -direction[0])

def turn_left(direction):
  return turn_right(turn_right(turn_right(direction)))

def get_item_at_position(maze, position):
  return maze[position[0]][position[1]]

def set_item_at_position(maze, position, value):
  maze[position[0]][position[1]] = value

def get_position_set_key(position):
  return str(position[0]) + '|' + str(position[1])

def find_shortest_path(maze, start_position, direction):
  position = start_position
  vertices_to_search = [[start_position, direction, set()]]
  visited_vertices = set()
  while len(vertices_to_search) > 0:
    [position, direction, shortest_path_vertices] = vertices_to_search.pop(0)
    if position in visited_vertices:
      continue

    visited_vertices.add(position)
    base_value = get_item_at_position(maze, position)

    forward_position = move(position, direction)
    forward_position_item = get_item_at_position(maze, forward_position)
    if forward_position_item in ['.', 'E']:
      set_item_at_position(maze, forward_position, base_value + 1)
    if type(forward_position_item) == int and forward_position_item > base_value + 1:
      shortest_path_vertices = shortest_path_vertices.union(set(forward_position))
      set_item_at_position(maze, forward_position, base_value + 1)

    right_position = move(position, turn_right(direction))
    right_position_item = get_item_at_position(maze, right_position)
    if right_position_item in ['.', 'E']:
      set_item_at_position(maze, right_position, base_value + 1001)
    if type(right_position_item) == int and right_position_item > base_value + 1001:
      set_item_at_position(maze, right_position, base_value + 1001)

    left_position = move(position, turn_left(direction))
    left_position_item = get_item_at_position(maze, left_position)
    if left_position_item in ['.', 'E']:
      set_item_at_position(maze, left_position, base_value + 1001)
    if type(left_position_item) == int and left_position_item > base_value + 1001:
      set_item_at_position(maze, left_position, base_value + 1001)

    if right_position_item != '#' and right_position not in visited_vertices:
      vertices_to_search.append([right_position, turn_right(direction)])
    if left_position_item != '#' and left_position not in visited_vertices:
      vertices_to_search.append([left_position, turn_left(direction)])
    if forward_position_item != '#' and forward_position not in visited_vertices:
      vertices_to_search.insert(0, [forward_position, direction])

def main():
  start = datetime.now()

  [maze, start_position, end_position] = get_maze()

  direction = (0, 1)
  set_item_at_position(maze, start_position, 0)

  find_shortest_path(maze, start_position, direction)

  cost = get_item_at_position(maze, end_position)
  end = datetime.now()

  diff = end - start
  print(diff)
  print(cost)

main()