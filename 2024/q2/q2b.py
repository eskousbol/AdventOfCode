def calculate_is_safe(row):
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
  return is_safe

def main():
  f = open("./q2_test_input.txt", "r")

  grid = []
  for line in f:
    grid.append(line.split(' '))

  safe_count = 0

  for row in grid:
    is_safe = calculate_is_safe(row)
    if is_safe:
      safe_count += 1
    else:
      is_safe = False
      for i in range(len(row)):
        new_row = row[:]
        del new_row[i]
        is_new_row_safe = calculate_is_safe(new_row)
        if (is_new_row_safe):
          safe_count += 1
          break

  print(safe_count)

main()