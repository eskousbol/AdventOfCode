import re

def parseFile():
  f = open("./q3_input.txt", "r")

  grid = []
  for line in f:
    grid.append(line.strip())
  return grid

def getNumbersInRow(row):
  regex_string = "\d+"
  numbers = re.search(regex_string, row)
  start_index = 0
  matches = {}
  while numbers:
    number_indices = numbers.span()
    number_value = numbers.group()
    for number_index in range(start_index + number_indices[0], start_index + number_indices[1]):
      matches[number_index] = int(number_value)
    start_index += number_indices[1]
    
    numbers = re.search(regex_string, row[start_index:])
  return matches

def checkForNumber(numbers, row_index, col_index, offsets):
  number_match = None
  new_row_index = row_index + offsets[0]
  if new_row_index in range(len(numbers)):
    matches = numbers[new_row_index]
  else:
    return number_match
  
  if col_index + offsets[1] in matches.keys():
    number_match = matches[col_index + offsets[1]]

  return number_match

def removeNumberFromRow(row, number, index, row_length):
  # Go back to get first
  new_row = dict(row)
  keys = row.keys()
  for i in list(reversed(range(0, index))):
    if i in keys:
      if new_row[i] == number:
        del new_row[i]
      else:
        break
    else:
      break

  for i in range(index, row_length):
    if i in keys:
      if new_row[i] == number:
        del new_row[i]
      else:
        break
    else:
      break

  return new_row

def main():
  grid = parseFile()

  total = 0
  numbers = []

  # Collect all the positions where there are numbers
  for i in range(len(grid)):
    row = grid[i]
    row_numbers = getNumbersInRow(row)
    numbers.append(row_numbers)

  directions = [(-1, 0), (-1, 1), (-1, -1), (1, 0), (1, 1), (1, -1), (0, 1), (0, -1)]

  for i in range(len(grid)):
    row = grid[i]
    for j in range(len(row)):
      if (ord(row[j]) < 48 or ord(row[j]) > 57) and ord(row[j]) != 46:
        symbol_index = j

        number = 0

        for direction in directions:
          number = checkForNumber(numbers, i, symbol_index, direction)
          if (number):
            numbers[i + direction[0]] = removeNumberFromRow(numbers[i + direction[0]], number, symbol_index + direction[1], len(row))
            total += number

  print(total)


main()