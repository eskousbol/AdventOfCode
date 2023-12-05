import re

def main():
  f = open("./q1_input.txt", "r")

  number_strings = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
  total = 0
  for line in f:
    numbers = re.findall("\d|" + "|".join(number_strings), line) 
    number_1 = number_strings.index(numbers[0]) if numbers[0] in number_strings else int(numbers[0])
    number_2 = number_strings.index(numbers[-1]) if numbers[-1] in number_strings else int(numbers[-1])

    total += ((number_1 * 10) + number_2)
  print(total)

main()