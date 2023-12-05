import re

def main():
  f = open("./q1_input.txt", "r")

  total = 0
  for line in f:
    numbers = re.findall("\d", line) 
    total += int(numbers[0]) * 10 + int(numbers[-1])
  print(total)

main()