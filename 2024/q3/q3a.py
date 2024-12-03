import re

def main():
  f = open("./q3_input.txt", "r")

  total = 0
  for line in f:
    muls = re.findall("mul\(\d{1,3},\d{1,3}\)", line)
    for mul in muls:
      numbers = re.findall("\d+", mul)
      total += int(numbers[0]) * int(numbers[1])
  print(total)

main()