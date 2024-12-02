def main():
  f = open("./q2_input.txt", "r")

  total_power = 0
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

    power = 1
    for key in game_data.keys():
      power *= game_data[key]

    total_power += power

  print(total_power)



main()