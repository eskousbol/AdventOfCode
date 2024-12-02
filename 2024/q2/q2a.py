def main():
  f = open("./q2_input.txt", "r")

  grid = []
  for line in f:
    grid.append(line.split(' '))

  safe_count = 0

  for row in grid:
    is_safe = True
    last_value = int(row[0])
    ascending = int(row[1]) - int(row[0]) > 0
    for val in row[1:]:
      if int(val) - last_value > 0 and not ascending:
        is_safe = False
      if int(val) - last_value < 0 and ascending:
        is_safe = False
      if last_value == int(val):
        is_safe = False
      if abs(last_value - int(val)) > 3:
        is_safe = False
      last_value = int(val)
    if is_safe:
      safe_count += 1

  print(safe_count)

main()