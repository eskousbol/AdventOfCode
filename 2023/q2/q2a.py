def main():
  f = open("./q2_input.txt", "r")

  maxes = {
    'blue': 14,
    'red': 12,
    'green': 13
  }

  total_possible = 0
  i = 1
  for line in f:
    game_data = {}
    all_games = line.split(':')[1]
    split_games = all_games.split(';')
    for game in split_games:
      handfuls = game.split(',')
      for cubes in handfuls:
        cubes_data = cubes.strip().split(' ')
        color = cubes_data[1]
        count = int(cubes_data[0])
        if color not in game_data.keys() or count > game_data[color]:
          game_data[color] = count

    is_possible = True
    for key in game_data.keys():
      if game_data[key] > maxes[key]:
        is_possible = False

    if is_possible:
      total_possible += i
    i += 1

  print(total_possible)



main()