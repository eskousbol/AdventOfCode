def holiday_hash(entry):
  value = 0
  for letter in entry:
    ascii_value = ord(letter)
    value += ascii_value
    value *= 17
    value = value % 256
  return value

def main():
  f = open("./q15_input.txt", "r")

  data = f.readline()

  entries = data.split(',')

  total = 0
  for entry in entries:
    total += holiday_hash(entry)

  print(total)

main()