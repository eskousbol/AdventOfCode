import re
from datetime import datetime

def main():
  start = datetime.now()
  f = open("./q13_input.txt", "r")

  a_button_regex = 'Button A: X\+(\d+), Y\+(\d+)'
  b_button_regex = 'Button B: X\+(\d+), Y\+(\d+)'
  prize_regex = 'Prize: X=(\d+), Y=(\d+)'

  a_x_offset = 0
  a_y_offset = 0
  a_cost = 3

  b_x_offset = 0
  b_y_offset = 0
  b_cost = 1

  x_prize = 0
  y_prize = 0

  result = 0
  i = 1
  for line in f:
    a_button = re.search(a_button_regex, line)
    if (a_button):
      a_x_offset = int(a_button.group(1))
      a_y_offset = int(a_button.group(2))

    b_button = re.search(b_button_regex, line)
    if (b_button):
      b_x_offset = int(b_button.group(1))
      b_y_offset = int(b_button.group(2))

    prize = re.search(prize_regex, line)
    if (prize):
      x_prize = int(prize.group(1)) + 10000000000000
      y_prize = int(prize.group(2)) + 10000000000000

      A = (b_y_offset / ((a_x_offset * b_y_offset) - (a_y_offset * b_x_offset))) * (x_prize - ((b_x_offset * y_prize)/ b_y_offset))
      B = (y_prize - (A * a_y_offset)) / b_y_offset
      if abs(A - round(A)) < 0.001 and abs(B - round(B)) < 0.001:
        result += round((a_cost * A) + (b_cost * B))
      i += 1

  
  end = datetime.now()
  diff = end - start
  print(diff.microseconds)
  print(result)

main()